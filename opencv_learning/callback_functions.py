import cv2


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Left button down at (', x, ', ', y, ')')
    elif event == cv2.EVENT_RBUTTONDOWN:
        print('Right button down at (', x, ', ', y, ')')
    elif event == cv2.EVENT_LBUTTONUP:
        print('Left button up at (', x, ', ', y, ')')
    elif event == cv2.EVENT_RBUTTONUP:
        print('Right button up at (', x, ', ', y, ')')


def trackbar_callback(value):
    print('Trackbar value:', value)


def keyboard_callback(event):
    if event == ord('q'):
        print('Quit')
        cv2.destroyAllWindows()


cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)
cv2.createTrackbar('trackbar', 'image', 0, 255, trackbar_callback)

while True:
    image = cv2.imread('lena.jpg')
    cv2.imshow('image', image)

    key = cv2.waitKey(1) & 0xFF
    if key != 255:
        keyboard_callback(key)

cv2.destroyAllWindows()
