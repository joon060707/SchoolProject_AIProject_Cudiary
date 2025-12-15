# calculate greenness index of an image
import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_greenness_index(image_path: str) -> float:

    web = False

    # path treatment for different environments
    if "http" in image_path:
        web = True
        image_path = "../fileserver/upload/" + image_path.split("upload/")[-1]

    print(f"Calculating greenness index for image: {image_path}")

    # use HSV color space to calculate greenness index
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image at {image_path}")
        return 0.0
    
    # 이미지 최적화
    max_dimension = 1024
    height, width = image.shape[:2]
    if max(height, width) > max_dimension:
        scaling_factor = max_dimension / float(max(height, width))
        image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # define range for green color in HSV
    # Hue: 30-85, Saturation: 20-255, Value: 40-255
    lower_green = np.array([30, 40, 40])
    upper_green = np.array([85, 255, 255])

    # create a mask for green color
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # reduce noise in the mask using morphological operations
    kernel = np.ones((10, 10), np.uint8) # increased kernel size for better noise reduction
    green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel)
    green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_CLOSE, kernel)

    # 시각화
    image_masked = cv2.bitwise_and(image, image, mask=green_mask)    
    # cv2.imwrite(image_path+"_image_masked.png", image_masked)
    # cv2.imwrite(image_path+"_green_mask.png", green_mask)

    
    # average greenness index calculation
    # greenness level = ExG = 2G - R - B
    B, G, R = cv2.split(image)
    ExG = 2 * G.astype(np.float32) - R.astype(np.float32) - B.astype(np.float32)

    # 초록색 부분만 경계 그리기
    contours, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, contours, -1, (255, 202, 118), 6) #BGR
    # cv2.imwrite(image_path+"_borders.png", image_with_contours)

    
    # define range for yellow/brown color in HSV
    lower_yellow = np.array([15, 40, 40])
    upper_yellow = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    yellow_mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_OPEN, kernel)
    yellow_mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_CLOSE, kernel)

    # draw yellow contours as well
    yellow_contours, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image_with_contours, yellow_contours, -1, (0, 255, 255), 6) #BGR
    cv2.imwrite(image_path+"_borders.png", image_with_contours) 



    # visualize ExG (for debugging purposes)

    # cv2.imwrite(image_path+"_ExG.png", ExG_normalized)

    if not web:
        ExG_normalized = ExG.astype(np.uint8)
        plot(image, green_mask, image_masked, ExG_normalized, image_with_contours)

    # calculate green pixels' average ExG value
    green_pixels = np.sum(green_mask > 0) # count of green pixels
    greenness_index = np.sum(ExG[green_mask > 0]) / (green_pixels + 1) # average ExG for green pixels

    return int(greenness_index) #, max(ExG[green_mask > 0].flatten()), min(ExG[green_mask > 0].flatten())


def plot(image, green_mask, image_masked, ExG_normalized, image_with_contours):
    image_masked_rgb = cv2.cvtColor(image_masked, cv2.COLOR_BGR2RGB)    
    plt.figure(figsize=(16, 8))
    plt.subplot(2, 3, 1)
    plt.imshow(image_masked_rgb)
    plt.title('Masked Green Areas')
    plt.axis('off')
    plt.subplot(2, 3, 2)
    plt.imshow(ExG_normalized, cmap='gray')
    plt.title('ExG')
    plt.axis('off')
    plt.subplot(2, 3, 3)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')
    plt.subplot(2, 3, 4)
    plt.imshow(image_with_contours[:,:,::-1])
    plt.title('Contours on Original Image')
    plt.axis('off')
    plt.subplot(2, 3, 5)
    plt.imshow(green_mask, cmap='gray')
    plt.title('Green Mask')
    plt.axis('off')
    plt.show()





if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python greenness.py <image_path>")
        sys.exit(1)

    for image_path in sys.argv[1:]:
        gi = calculate_greenness_index(image_path)
        print(f"Greenness Index for {image_path}: {gi}")