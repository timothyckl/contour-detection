import numpy as np
import cv2 as cv

image_with_obj = cv.imread('./assets/image_with_objects.JPG')
rotated_image = cv.rotate(image_with_obj, cv.ROTATE_90_COUNTERCLOCKWISE)
gray_image = cv.cvtColor(rotated_image, cv.COLOR_BGR2GRAY)
width, height = gray_image.shape

# blur images to smooth out noise and make it easier to detect edges
blurred_image_with_obj = cv.blur(gray_image, (10, 10)) 

# apply threshold to make image binary
ret, thresh_image_with_obj = cv.threshold(blurred_image_with_obj, thresh=127, \
        maxval=255, type=0)

# find contours
contours, hierarchy = cv.findContours(thresh_image_with_obj, mode=cv.RETR_TREE, \
        method=cv.CHAIN_APPROX_SIMPLE)

# draw contours
cv.drawContours(rotated_image, contours, contourIdx=-1, color=[0, 255, 0], \
        thickness=20)

# resize images
# image_with_obj = cv.resize(rotated, (0, 0), fx=0.5, fy=0.5)

# show images
cv.imshow('image', rotated_image)
cv.imshow('threshold', thresh_image_with_obj)

# save images
cv.imwrite('./assets/contoured_image.jpg', rotated_image)
cv.imwrite('./assets/threshold_image.jpg', thresh_image_with_obj)

cv.waitKey(0)
cv.destroyAllWindows()
