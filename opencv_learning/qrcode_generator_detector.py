import cv2
from pyzbar import pyzbar
import qrcode

def qr_generate(data):
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color="black", back_color="white")
    img_qr.save('qrcode.jpg')


def qr_detect(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    qrcode = pyzbar.decode(img_gray)
    for code in qrcode:
        (x, y, w, h) = code.rect
        data = code.data.decode("utf-8")
        qr_type = code.type

        cv2.rectangle(img, (x-10, y-10), (x+w+10, y+h+10), (0, 255, 0), 2)
        cv2.putText(img, data, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

qr_generate("hello world")
img=cv2.imread('qrcode.jpg')
qr_detect(img)
cv2.imshow("QR Code Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
