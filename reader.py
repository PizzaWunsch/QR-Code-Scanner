import cv2
import webbrowser
from pyzbar import pyzbar

windowName = "QR-Code Scanner >> [ESC] zum beenden"
cameraNumber = 0

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        barcode_info = barcode.data.decode('utf-8')
        webbrowser.open(barcode_info)
        with open("barcode_result.txt", mode ='w') as file:
            file.write("Erkannter Barcode:" + barcode_info)
    return frame

def main():

    camera = cv2.VideoCapture(cameraNumber)
    ret, frame = camera.read()

    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) == 27:
            break
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
