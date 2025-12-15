from typing import Tuple
import torch
from torch.utils.data import DataLoader
from torchvision import transforms, datasets
from torchvision.models import mobilenet_v3_small, MobileNet_V3_Small_Weights
from torchvision.models import mobilenet_v3_small


import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm

# Try modern torchvision weights API, fall back to legacy pretrained flag
try:
    def _mobilenet_v3_small(pretrained: bool):
        weights = MobileNet_V3_Small_Weights.IMAGENET1K_V1 if pretrained else None
        return mobilenet_v3_small(weights=weights)
except Exception:
    def _mobilenet_v3_small(pretrained: bool):
        return mobilenet_v3_small(pretrained=pretrained)


# Default hyperparameters / settings (follow project conventions)
IMG_SIZE = 224
BATCH_SIZE = 16
EPOCHS = 20
LR = 0.0003
WEIGHT_DECAY = 0.05
NUM_CLASSES = 3  # leaf / flower / fruit
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


class TypeClassifier(nn.Module):
    """
    MobileNet-v3 based classifier for 3 classes.
    Accepts RGB image tensors shaped (B,3,H,W) where H,W will be resized beforehand.
    """
    def __init__(self, num_classes: int = NUM_CLASSES, pretrained: bool = True):
        super().__init__()
        self.backbone = _mobilenet_v3_small(pretrained=pretrained)
        # replace final linear layer to match num_classes
        # classifier is usually nn.Sequential(Linear(in, hidden), Hardswish, Dropout, Linear(hidden, out))
        # we keep previous hidden dims and replace last layer
        try:
            feat_dim = self.backbone.classifier[0].in_features  # input feature dim of first linear
            hidden_dim = self.backbone.classifier[0].out_features
            self.backbone.classifier[-1] = nn.Linear(hidden_dim, num_classes)
        except Exception:
            # fallback: inspect last linear
            for i, m in enumerate(self.backbone.classifier):
                if isinstance(m, nn.Linear):
                    last_idx = i
            in_f = self.backbone.classifier[last_idx].in_features
            self.backbone.classifier[last_idx] = nn.Linear(in_f, num_classes)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.backbone(x)


def create_transforms(img_size: int = IMG_SIZE) -> Tuple[transforms.Compose, transforms.Compose]:
    """
    Return (train_transform, val_transform).
    Images are resized to img_size to fit MobileNet-v3 input.
    Normalization uses ImageNet mean/std as project convention.
    """
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]

    train_tf = transforms.Compose([
        transforms.Resize(int(img_size * 1.1)),
        transforms.RandomResizedCrop(img_size, scale=(0.7, 1.0)),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.02),
        transforms.RandomGrayscale(p=0.05),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=mean, std=std),
    ])

    val_tf = transforms.Compose([
        transforms.Resize((img_size, img_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=mean, std=std),
    ])

    return train_tf, val_tf


def make_dataloaders(
    train_dir: str,
    val_dir: str,
    batch_size: int = BATCH_SIZE,
    num_workers: int = 4,
    pin_memory: bool = True
) -> Tuple[DataLoader, DataLoader]:
    """
    Create dataloaders from ImageFolder-structured directories.
    Directory structure:
        train_dir/class_x/xxx.png
        train_dir/class_y/yyy.png
    """
    train_tf, val_tf = create_transforms()
    train_ds = datasets.ImageFolder(train_dir, transform=train_tf)
    val_ds = datasets.ImageFolder(val_dir, transform=val_tf)

    train_loader = DataLoader(
        train_ds, batch_size=batch_size, shuffle=True,
        num_workers=num_workers, pin_memory=pin_memory
    )
    val_loader = DataLoader(
        val_ds, batch_size=batch_size, shuffle=False,
        num_workers=num_workers, pin_memory=pin_memory
    )
    return train_loader, val_loader


# using tqdm

def train_epoch(model: nn.Module, loader: DataLoader, optimizer, criterion, device: str = DEVICE, use_amp: bool = True):
    model.train()
    running_loss = 0.0
    scaler = torch.amp.GradScaler(enabled=(use_amp and device.startswith("cuda")))
    with tqdm(loader, unit="batch") as loader_tqdm:
        loader_tqdm.set_description("Training")

        for imgs, targets in loader_tqdm:
            imgs = imgs.to(device, non_blocking=True)
            targets = targets.to(device, non_blocking=True)

            optimizer.zero_grad()
            with torch.amp.autocast(device_type="cuda", enabled=(use_amp and device.startswith("cuda"))):
                logits = model(imgs)
                loss = criterion(logits, targets)
            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()

        running_loss += loss.item() * imgs.size(0)
    return running_loss / len(loader.dataset)


@torch.no_grad()
def validate_epoch(model: nn.Module, loader: DataLoader, criterion, device: str = DEVICE):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0
    for imgs, targets in loader:
        imgs = imgs.to(device, non_blocking=True)
        targets = targets.to(device, non_blocking=True)
        logits = model(imgs)
        loss = criterion(logits, targets)
        running_loss += loss.item() * imgs.size(0)
        preds = logits.argmax(dim=1)
        correct += (preds == targets).sum().item()
        total += imgs.size(0)
    return running_loss / len(loader.dataset), correct / total


def train(
    train_dir: str,
    val_dir: str,
    out_path: str = "typeclassifier_best.pt",
    epochs: int = EPOCHS,
    lr: float = LR,
    weight_decay: float = WEIGHT_DECAY,
    num_classes: int = NUM_CLASSES,
    device: str = DEVICE
):
    model = TypeClassifier(num_classes=num_classes, pretrained=True)
    model = model.to(device)

    train_loader, val_loader = make_dataloaders(train_dir, val_dir)
    optimizer = optim.AdamW(model.parameters(), lr=lr, weight_decay=weight_decay)
    criterion = nn.CrossEntropyLoss()

    best_acc = 0.0
    for epoch in range(1, epochs + 1):
        train_loss = train_epoch(model, train_loader, optimizer, criterion, device)
        val_loss, val_acc = validate_epoch(model, val_loader, criterion, device)

        print(f"Epoch {epoch}/{epochs}  train_loss={train_loss:.4f}  val_loss={val_loss:.4f}  val_acc={val_acc:.4f}")

        if val_acc > best_acc:
            best_acc = val_acc
            torch.save({
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "epoch": epoch,
                "val_acc": val_acc
            }, out_path)
            print(f"Saved best model (val_acc={val_acc:.4f}) -> {out_path}")


def load_model(checkpoint_path: str, device: str = DEVICE, num_classes: int = NUM_CLASSES) -> nn.Module:
    model = TypeClassifier(num_classes=num_classes, pretrained=False)
    ckpt = torch.load(checkpoint_path, map_location=device)
    model.load_state_dict(ckpt["model_state_dict"])
    model.to(device)
    model.eval()
    return model


if __name__ == "__main__":    
    # Minimal example: set TRAIN_DIR and VAL_DIR to your ImageFolder dataset paths before running
    TRAIN_DIR = "D:\\AIHub\\dataset\\TypeClassifier\\Train"
    VAL_DIR = "D:\\AIHub\\dataset\\TypeClassifier\\Val"
    train(TRAIN_DIR, VAL_DIR)
