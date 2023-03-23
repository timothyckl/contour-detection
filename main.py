import numpy as np
import cv2 as cv

image_with_obj = cv.imread('./assets/image_with_objects.JPG')
gray_image = cv.cvtColor(image_with_obj, cv.COLOR_BGR2GRAY)
# black_image = np.zeros(image_with_obj.shape, dtype=np.uint8)

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
cv.drawContours(image_with_obj, contours, contourIdx=-1, color=[0, 255, 0], \
        thickness=20)

# resize images
# image_with_obj = cv.resize(image_with_obj, (0, 0), fx=0.5, fy=1)
# black_image[:height, :width//2] = image_with_obj

# print(image_with_obj.shape)
# print(black_image.shape)

# cv.imshow('contour', black_image[:height, :width//2])
cv.imshow('image', image_with_obj)
cv.imshow('threshold', thresh_image_with_obj)


cv.waitKey(0)
cv.destroyAllWindows()
