#Drawing on images

import cv2

image = cv2.imread('images/image.jpg')

# Draw rectangle (from the point 50 to the point 200), (color green), (thickness of rectangle)
cv2.rectangle(image, (50, 50), (200, 200), (0, 255, 0), 2)

# Draw circle (center of the circle 300,150), (radius=50), (color blue), (thickness 2)
cv2.circle(image, (300, 150), 50, (255, 0, 0), 2)

# Add text (text to show), (starting position (x=50)(y=300)), (font style), (fontsize=1), (color red), (thickness=2)
cv2.putText(image, 'OpenCV', (50, 300),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 0, 255), 2)

cv2.imshow('Drawing', image)

#save image
cv2.imwrite('drawing.png', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
