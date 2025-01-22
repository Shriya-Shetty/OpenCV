import cv2
import numpy as np

img_path=r"C:\Users\Shriya\Desktop\Extracurricular\TMRT WORK\Vr_person.jpg"
img=cv2.imread(img_path)
img=cv2.resize(img,(1200,750))
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#with kernel 50*50
img_blur=cv2.blur(img,(50,50))
cv2.imshow("Blurred Image",img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_blur_1=cv2.boxFiller(img,-1,(50,50), normalize=False)
cv2.imshow("Blurred Image 1",img_blur_1)
cv2.waitKey(0)
cv2.destroyAllWindows()