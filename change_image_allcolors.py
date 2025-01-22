import cv2

img_path = r"C:\Users\Shriya\Desktop\Extracurricular\TMRT WORK\Vr_person.jpg"
img = cv2.imread(img_path)
img_resize = cv2.resize(img, (1200, 720))

colors = [cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2HLS, cv2.COLOR_BGR2YUV]

for color in colors:
    color_img = cv2.cvtColor(img_resize, color)
    cv2.imshow("image", color_img)
    cv2.waitKey(2000)

cv2.destroyAllWindows()