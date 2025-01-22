import cv2

img_path = "Vr_person.jpg"
img = cv2.imread(img_path)
img_resize = cv2.resize(img, (1200, 720))

# Display the image
cv2.imshow("Image", img_resize)

# Print the first 10 elements of each channel
print("Blue channel (first 10 elements):", img_resize[:, :, 0][:10])
print("Green channel (first 10 elements):", img_resize[:, :, 1][:10])
print("Red channel (first 10 elements):", img_resize[:, :, 2][:10])

# Keep the window open until a key is pressed
cv2.waitKey(0)

# Close the window
cv2.destroyAllWindows()