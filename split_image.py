import cv2
import time

img_path=r"C:\Users\Shriya\Desktop\Extracurricular\TMRT WORK\Vr_person.jpg"
img=cv2.imread(img_path)
img=cv2.resize(img,(1200,750))
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Split using numpy indexing
print(img)
print(img.shape)
print(img[:,:,2]) #color channels for red
print(img[:,:,2].shape) #color channels for red
b, g, r =cv2.split(img)
cv2.imshow("Blue img",b)
cv2.imshow("green img",g)
cv2.imshow("red img",r)
cv2.waitKey(0)
cv2.destroyAllWindows()


start_time=time.time()
for i in range(100):
    #r,g,r= cv2.split(img)
    b=img[:,:,0]
    g=img[:,:,1]
    r=img[:,:,2]
end_time=time.time()
print("Time taken for execution is ",end_time-start_time)

#Show Single Channel
cv2.imshow("Model",img[:,:,0])
cv2.waitKey(0)
cv2.destroyAllWindows()