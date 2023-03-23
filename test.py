import numpy as np
import cv2 as cv

bottle_image = cv.imread('assets/with_bottle.JPG', cv.IMREAD_GRAYSCALE)
black_image = np.zeros(bottle_image.shape, np.uint8)
resized_black_image = cv.resize(black_image, (0, 0), fx=2, fy=1)
frame_height, frame_width = resized_black_image.shape

resized_black_image[:, :frame_width//2] = bottle_image
# resized_black_image[:, frame_width//2:] = bottle_image

cv.imshow('black', resized_black_image)
# cv.imshow('bottle', bottle_image)
cv.waitKey(0)
cv.destroyAllWindows()
