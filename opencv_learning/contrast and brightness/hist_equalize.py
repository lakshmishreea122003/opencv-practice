import cv2 as cv

img1 = cv.imread('lena.jpg', 0)

# Histogram equalization
img2 = cv.equalizeHist(img1)

# CLAHE
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
img3 = clahe.apply(img1)

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('img3', img3)

cv.waitKey(0)
cv.destroyAllWindows()
