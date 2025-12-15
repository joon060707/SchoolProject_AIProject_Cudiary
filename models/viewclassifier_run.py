# load the model
import torch
import torch.nn as nn
import viewclassifier
import json
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
from torchvision import transforms, datasets
from tqdm import tqdm

CLASS_NAMES = ['Single organ', 'Whole plant']  # Example class names

# test and calculate the accuracy, and show the confusion matrix with matplotlib
def test_model(model: nn.Module, device: str = "cuda"):

    test_dir = "D:\\AIHub\\dataset\\ViewClassifier\\Test"  # path to test dataset
    batch_size = 32
    num_workers = 4
    pin_memory = True

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), # using same normalization as training
    ])

    test_ds = datasets.ImageFolder(test_dir, transform=transform)
    test_loader = DataLoader(
        test_ds, batch_size=batch_size, shuffle=False,
        num_workers=num_workers, pin_memory=pin_memory
    )

    # evaluation
    model.eval()
    correct = 0
    total = 0
    all_preds = []
    all_labels = []
    with torch.no_grad():
        with tqdm(test_loader, unit="batch") as loader_tqdm:
            loader_tqdm.set_description("Testing")
            for images, labels in loader_tqdm:
                images = images.to(device)
                labels = labels.to(device)
                outputs = model(images)
                _, predicted = torch.max(outputs.data, 1)

                total += labels.size(0)
                correct += (predicted == labels).sum().item()
                all_preds.extend(predicted.cpu().numpy())
                all_labels.extend(labels.cpu().numpy())
                loader_tqdm.set_postfix(accuracy=100.*correct/total)
                
    accuracy = correct / total

    print(f"Test Accuracy: {accuracy*100:.2f}%")
    # plot confusion matrix
    import matplotlib.pyplot as plt
    from sklearn.metrics import confusion_matrix
    import numpy as np
    cm = confusion_matrix(all_labels, all_preds)
    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.colorbar()
    tick_marks = np.arange(len(CLASS_NAMES))
    plt.xticks(tick_marks, CLASS_NAMES, rotation=45)
    plt.yticks(tick_marks, CLASS_NAMES)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.tight_layout()
    plt.show()
    plt.savefig("viewclassifier_confusion_matrix.png")


    return accuracy, all_labels, all_preds





# inference: load an image and predict its class
if __name__ == "__main__":

    import sys
    MODEL_PATH = "viewclassifier_best.pt"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = viewclassifier.load_model(MODEL_PATH, device=device)
    model.eval()

    # take an image path as command line argument
    if len(sys.argv) != 2:
        # run a test
        print("No image path provided. Running test on test dataset...")
        test_model(model, device=device)
        sys.exit(0)
    else:
        IMAGE_PATH = sys.argv[1]

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), # using same normalization as training
    ])
    image = Image.open(IMAGE_PATH).convert("RGB")
    input_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        predicted_class = CLASS_NAMES[probabilities.argmax().item()]
        confidence = probabilities.max().item()
    # print(f"Predicted class: {predicted_class} with confidence {confidence:.4f}")   

    # return the predicted class and confidence as json

    result = {
        "predicted_class": predicted_class,
        "confidence": f"{confidence:.4f}"
    }
    print(json.dumps(result))




def infer(image_path: str) -> str:

    # print(f"Original image path: {image_path}")
    # if(image_path.startswith("D:")):
    #     image_path = "../fileserver/" + image_path.split("upload\\")[-1]
    # print(f"Adjusted image path: {image_path}")


    MODEL_PATH = "viewclassifier_best.pt"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = viewclassifier.load_model(MODEL_PATH, device=device)
    model.eval()
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), # using same normalization as training
    ])


    # path treatment
    image_path = "../fileserver/upload/" + image_path.split("upload/")[-1]

    image = Image.open(image_path).convert("RGB")
    input_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        predicted_class = CLASS_NAMES[probabilities.argmax().item()]
        confidence = probabilities.max().item()
    result = {
        "predicted_class": predicted_class,
        "confidence": f"{confidence:.4f}"
    }
    import json
    return json.dumps(result)

