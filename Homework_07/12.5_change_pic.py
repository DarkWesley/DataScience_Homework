import cv2
image_path = r'D:\pic.jpg'
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
new_size = (500,300)
processed_image = cv2.resize(gray_image, new_size)
output_path='output_image.jpg'
cv2.imwrite(output_path, processed_image)
cv2.imshow('original picture', image)
cv2.imshow('grey picture', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()