#Image transformations

import cv2

image = cv2.imread('images/image.jpg')
# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur
blur = cv2.GaussianBlur(image, (5, 5), 0)

# Resize
resize = cv2.resize(image, (300, 300))

# Rotate
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotate = cv2.warpAffine(image, matrix, (w, h))

# Display
cv2.imshow('Original', image)
cv2.imshow('Gray', gray)
cv2.imshow('Blur', blur)
cv2.imshow('Resize', resize)
cv2.imshow('Rotate', rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()

#This task applies basic transformations. Grayscale reduces color complexity, Gaussian blur smooths noise,
#resizing changes dimensions, and rotation uses transformation matrices to rotate the image.