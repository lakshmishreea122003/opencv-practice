# import cv2
#
# img=cv2.imread('lena.jpg')
# cv2.waitKey(4000)
# cv2.imshow('image',img)

# import cv2
# img = cv2.imread('lena.jpg')
# img[0:100,0:100]=img[200:400,100:200]
# a=img[200:300,100:200]
# img[100:200,100:200]=a
# img[:,:,2] = 0
# border = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP, value=[0,0,0])
# blue=img[10,10,2]
# print(blue)
# print(img.item(10,10,2))
# img.itemset((10,10,2),100)
# print(img.item(10,10,2))
# mean_value = cv2.mean(img)
# print(mean_value)
# img[0:100,0:100] = [0,0,0]
# print(img)
# Apply a binary threshold to the image
# thresh_value = 127
# max_value = 255
# retval, binary_img = cv2.threshold(img, thresh_value, max_value, cv2.THRESH_BINARY_INV)
# cv2.imshow('image', img)
# cv2.imshow('image', binary_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Video + object detect
# import cv2 as cv
# import numpy as np
# cap = cv.VideoCapture(0)
# while(1):
#     # Take each frame
#     _, frame = cap.read()
#     # Convert BGR to HSV
#     hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
#     # define range of blue color in HSV
#     # lower_blue = np.array([110,50,50])
#     # upper_blue = np.array([130,255,255])
#     lower_red = np.array([0, 50, 50])
#     upper_red = np.array([10, 255, 255])
#     # Threshold the HSV image to get only blue colors
#     mask = cv.inRange(hsv, lower_red, upper_red)
#     # Bitwise-AND mask and original image
#     res = cv.bitwise_and(frame,frame, mask= mask)
#     cv.imshow('frame',frame)
#     cv.imshow('mask',mask)
#     cv.imshow('res',res)
#     k = cv.waitKey(5) & 0xFF
#     if k == 27:
#         break
# cv.destroyAllWindows()

# import cv2
#
# # Load image with alpha channel
# img = cv2.imread('Vishal-painting.png', cv2.IMREAD_UNCHANGED)
#
# # Check if image has an alpha channel
# if img.shape[2] == 4:
#     # Split image into RGB and alpha channels
#     bgr = img[:,:,0:3]
#     alpha = img[:,:,3]
#
#     # Create mask from alpha channel
#     mask = cv2.threshold(alpha, 0, 255, cv2.THRESH_BINARY)[1]
#
#     # Apply mask to RGB channels
#     bgr = cv2.bitwise_and(bgr, bgr, mask=mask)
#
#     # Combine channels back into image with alpha channel
#     img = cv2.merge([bgr, mask])
#
# # Display image with alpha channel
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2 as cv
#
# cap=cv.VideoCapture(0)
#
# while(1):
#     _,frame=cap.read()
#     ret, thresh = cv.threshold(frame, 100, 255, cv.THRESH_BINARY)
#     cv.imshow("black&white",thresh)
#
#     if cv.waitKey(5) & 0xFF ==27:
#         break
# cv.destroyAllWindows()


#Alpha Blending
# import cv2
#
# img1 = cv2.imread('blue.jpg')
# img2 = cv2.imread('lena.jpg')
#
# img2 = cv2.resize(img2, img1.shape[1::-1])
#
# cv2.imshow("img 1",img1)
#
# cv2.waitKey(0)
#
# cv2.imshow("img 2",img2)
#
# cv2.waitKey(0)
#
# choice = 1
#
# while (choice) :
#
# 	alpha = float(input("Enter alpha value"))
#
# 	dst = cv2.addWeighted(img1, alpha , img2, 1-alpha, 0)
#
# 	cv2.imwrite('alpha_mask_.png', dst)
#
# 	img3 = cv2.imread('alpha_mask_.png')
#
# 	cv2.imshow("alpha blending 1",img3)
#
# 	cv2.waitKey(3000)
# 	dst1 = cv2.addWeighted(img1, alpha , img2, 1-alpha, 50)
#
# 	cv2.imwrite('alpha_mask1_.png', dst)
#
# 	img4 = cv2.imread('alpha_mask1_.png')
#
# 	cv2.imshow("alpha blending 1",img4)
#
# 	cv2.waitKey(0)

	# choice = int(input("Enter 1 to continue and 0 to exit"))

# import cv2 as cv
# import numpy as np

# colourful img
# img = np.random.randint(0, 256, (480, 640, 3), dtype=np.uint8)

# print(img)
# cv.imshow("image",img)

# cv.waitKey(0)
# cv.destroyAllWindows()


# # smoothening the image
# 1
# import cv2

# # Load the image
# img = cv2.imread('lena.jpg')
#
# # Apply Gaussian blur with a 5x5 kernel and a sigma value of 0
# img_smooth = cv2.GaussianBlur(img, (5, 5), 50)
#
# # Display the original and smoothed images side by side
# cv2.imshow('Original Image', img)
# cv2.imshow('Smoothed Image', img_smooth)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# edge
# importing the modules needed
# import cv2
# import numpy as np
#
# # Reading the image
# image = cv2.imread('lena.jpg')
#
# # Creating the kernel(2d convolution matrix)
# kernel2 = np.array([[-1, -1, -1],
# 					[-1, 8, -1],
# 					[-1, -1, -1]])
#
# # Applying the filter2D() function
# img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)
#
# img3=cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)[1]
# # img4=cv2.bitwise_not(img)
# # Shoeing the original and output image
# cv2.imshow('Original', img3)
# cv2.imshow('Kernel Blur', img)
#
# cv2.waitKey()
# cv2.destroyAllWindows()

# #denoising
# import cv2
#
# # Reading the image
# image = cv2.imread('lena.jpg')
#
# # Applying Fast Non-Local Means Denoising
# img_denoised = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
#
# # Showing the original and denoised image
# cv2.imshow('Original', image)
# cv2.imshow('Denoised', img_denoised)
#
# cv2.waitKey()
# cv2.destroyAllWindows()

##
# increase the sharpness of the image
# import cv2
# import numpy as np
#
# # Load the image
# img = cv2.imread('lena.jpg')
#
# # Define the sharpening filter kernel
# # kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
#
# # Apply the sharpening filter
# # sharp_img = cv2.filter2D(img, -1, kernel)
# cv2.rectangle(img, (0,0), (100,100), (0, 0, 0))
# # Display the sharpened image
# cv2.imshow('Sharpened Image', img)
# cv2.waitKey(0)
#
# import numpy as np
# import cv2

# resize
import cv2
import numpy as np

image = cv2.imread(r"D:\sims\eb\sim21\EB-ML-06-10-2022-Test-Output-15\PERFORATION\Overkill\Fail\Blister 1 2022-03-12 12-59-43.859 T0 M0 G0 3 PERFORATION Mono.bmp", 1)
# Loading the image

half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
bigger = cv2.resize(image, (1050, 1610))

stretch_near = cv2.resize(image, (780, 540),
			interpolation = cv2.INTER_LINEAR)


Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[image, half, bigger, stretch_near]
count = 4

for i in range(count):
	plt.subplot(2, 2, i + 1)
	plt.title(Titles[i])
	plt.imshow(images[i])

plt.show()







