import cv2

#grey filter
def grey_filter(image_path):
    img = cv2.imread(image_path)
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return grey_img



 # # img1=cv2.imshow('image',img)
 #    cv2.imshow('image', img)
 #    cv2.waitKey(1000)
 #    cv2.imwrite('./lena.png', img)
 #
 #    cv2.destroyAllWindows()