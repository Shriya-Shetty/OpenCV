import cv2
import numpy as np
img_path=r"C:\Users\Shriya\Desktop\Extracurricular\TMRT WORK\road_marking.jpg"
img=cv2.imread(img_path)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#convert image in gray scale
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray img",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
#road margin detection using gray scale
gray_img_copy=np.copy(img_gray)
gray_img_copy[gray_img_copy[:,:]<200]=0
cv2.imshow("Image",gray_img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
#road margin detection using color image 
img_copy=np.copy(img)
print(img_copy.shape)
img_copy[(img_copy[:,:,0]<200)|(img_copy[:,:,1]<200)|(img_copy[:,:,2]<200)]=0 
cv2.imshow("Image",img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()