import cv2

img_path = "Vr_person.jpg"
img = cv2.imread(img_path)
img_resize = cv2.resize(img, (1200, 720))

img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow("Grayscale Image", img_gray) 
cv2.waitKey(0)
cv2.destroyAllWindows()