import cv2 as cv
import numpy as np

image = cv.imread('lena.jpg')

gamma=2.2
gamma_inv=1/gamma
# for brighter image
table1 = np.array([(i/255.0)**gamma*255 for i in np.arange(0, 256)]).astype('uint8')

# to decrease brightness of image
table2 = np.array([(i/255.0)**gamma_inv*255 for i in np.arange(0, 256)]).astype('uint8')

bright_image=cv.LUT(image, table1)
dull_image=cv.LUT(image, table2)
cv.imshow('Original Image', image)
cv.imshow('bright_image', bright_image)
cv.imshow('dull_image', dull_image)
# Wait until user press some key
cv.waitKey()
