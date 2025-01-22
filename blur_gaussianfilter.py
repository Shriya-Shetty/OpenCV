import cv2
import numpy as np

img_path=r"C:\Users\Shriya\Desktop\Extracurricular\TMRT WORK\Vr_person.jpg"
img=cv2.imread(img_path)
img=cv2.resize(img,(1200,750))
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()