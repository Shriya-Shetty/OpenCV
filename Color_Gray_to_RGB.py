import cv2
import numpy as np

# Load the image
img_path = r"C:\Users\Shriya\Desktop\Extracurricular\TMRT WORK\Vr_person.jpg"
img = cv2.imread(img_path)
cv2.imshow("Original Image", img)
cv2.waitKey(0)

# Convert color/grayscale to RGB
if len(img.shape) == 2:  # Grayscale image (has only one channel)
    # Create an RGB image by stacking three identical grayscale channels
    rgb_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
else:  # Color image (already in BGR format)
    # Convert BGR to RGB
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the converted RGB image
cv2.imshow("RGB Image", rgb_img)
cv2.waitKey(0)

cv2.destroyAllWindows()