#morphological operations-Erosion and Dilation
import cv2
import numpy as np
img_path=r"C:\Users\Shriya\Desktop\Extracurricular\TMRT WORK\road_marking.jpg"
img=cv2.imread(img_path)
img=cv2.resize(img,(600,400))
cv2.imshow("Original image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel1=np.ones((5,5),dtype="uint8")
erode_img=cv2.erode(img,kernel1,iterations=2)
img_erodeimg=np.hstack((img,erode_img))
cv2.imshow("Both image",img_erodeimg)
cv2.waitKey(0)
cv2.destroyAllWindows()