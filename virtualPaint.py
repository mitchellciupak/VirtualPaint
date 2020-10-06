import cv2
import numpy as np

# Macros
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

myColors = [[5,107,0,19,255,255], #Orange
            [133,56,0,159,156,255], #Purple
            [57,76,0,100,255,255]] #Green

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper) #color that you want as white and everything else as white
        cv2.imshow(str(color[0]), mask)


## Cap import
cap = cv2.VideoCapture(0)
cap.set(3, FRAME_WIDTH)
cap.set(4, FRAME_HEIGHT)
cap.set(propId=10,value=150) #brightness

while True:
    isValid, img = cap.read()

    findColor(img, myColors)


    cv2.imshow("Output", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

