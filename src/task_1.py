##Image Read and Display

#[This task demonstrates how to load an image using OpenCV and display it in a window. The imread() 
#function reads the image, while imshow() displays it. The imwrite() function is used to save the image in a
# different format (PNG in this case).]

import cv2

# Read image
image = cv2.imread('images/image.jpg')

# Display image
cv2.imshow('Original Image', image)

# Save image in different format
cv2.imwrite('output.png', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

