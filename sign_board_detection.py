import cv2
import numpy as np

# Load the image
img_path = r"C:\Users\Shriya\Desktop\Extracurricular\TMRT WORK\road_marking.jpg"
img = cv2.imread(img_path)

# Show the original image
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Road margin detection using grayscale
gray_copy = np.copy(gray)
gray_copy[gray_copy[:, :] < 200] = 0  # Thresholding for lighter colors
cv2.imshow("Grayscale Margin Detection", gray_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Road margin detection using color image
color_copy = np.copy(img)
# Thresholding for lighter colors in all color channels
color_copy[(color_copy[:, :, 0] < 200) | (color_copy[:, :, 1] < 200) | (color_copy[:, :, 2] < 200)] = 0
cv2.imshow("Color Margin Detection", color_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Yellow pixel extraction (approximate)
yellow_lower = np.array([20, 100, 100])  # Lower bound for yellow in HSV
yellow_upper = np.array([30, 255, 255])  # Upper bound for yellow in HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
yellow_pixels = cv2.bitwise_and(img, img, mask=yellow_mask)
cv2.imshow("Yellow Pixel Extraction", yellow_pixels)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Red pixel extraction (approximate)
red_lower = np.array([0, 120, 70])  # Lower bound for red in HSV
red_upper = np.array([10, 255, 255])  # Upper bound for red in HSV
red_mask = cv2.inRange(hsv, red_lower, red_upper)
red_pixels = cv2.bitwise_and(img, img, mask=red_mask)
cv2.imshow("Red Pixel Extraction", red_pixels)
cv2.waitKey(0)
cv2.destroyAllWindows()

# All color extraction (using inverse thresholding)
color_copy_all = np.copy(img)
color_copy_all[(color_copy_all[:, :, 0] >= 200) & (color_copy_all[:, :, 1] >= 200) & (color_copy_all[:, :, 2] >= 200)] = 0 
cv2.imshow("All Color Extraction", color_copy_all)
cv2.waitKey(0)
cv2.destroyAllWindows()