import cv2
import time


img_path=r"C:\Users\Shriya\Desktop\Extracurricular\TMRT WORK\Vr_person.jpg"
img=cv2.imread(img_path)
img=cv2.resize(img,(1200,750))

b,g,r=cv2.split(img)
img_merge= cv2.merge([b,g,r])
cv2.imshow("Image merged",img_merge)
print(img_merge.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()