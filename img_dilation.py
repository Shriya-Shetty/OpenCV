import cv2
import numpy as np

img_path="road_marking.jpg"
img=cv2.imread(img_path)
img=cv2.resize(img,(600,400))
cv2.imshow("Original image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel1=np.ones((5,5),dtype="uint8")
dilated_img=cv2.dilate(img,kernel1,iterations=1)
both_img=np.hstack((img,dilated_img))
cv2.imshow("Both image",both_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
