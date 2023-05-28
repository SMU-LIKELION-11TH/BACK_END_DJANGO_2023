import cv2
import numpy as np
import matplotlib.pyplot as pit

live_Camera = cv2.VideoCapture(0)
while(live_Camera.isOpened()):
    ret, frame = live_Camera.read()
    cv2.imshow("Fire Detection", frame)
    if cv2.waitkey(10) == 27:
        break
img_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
img_cap = pit.imshow(img_RGB)
pit.show()
live_Camera.release()
cv2.destroyAllWindows()