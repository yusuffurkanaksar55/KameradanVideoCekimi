import cv2
import numpy as np

kamera=cv2.VideoCapture(0)


while True:
    ret,kare=kamera.read()
    
    cv2.imshow("ekran",kare)
    
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

kamera.release()

cv2.destroyAllWindows()
