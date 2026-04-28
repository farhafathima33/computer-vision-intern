#Edge Detection

import cv2

image = cv2.imread('images/image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny edge detection
edges = cv2.Canny(gray, 50, 150)

cv2.imshow('Edges', edges)

#save image
cv2.imwrite('edges.png', image)

cv2.waitKey(0)
cv2.destroyAllWindows()