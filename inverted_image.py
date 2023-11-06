import cv2

image = cv2.imread("235.jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_image = 255 - gray_image
cv2.imshow("Inverted Image", inverted_image)
cv2.waitKey(0)