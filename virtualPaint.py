import cv2
import numpy as np

# Macros
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Please see ./colorCalibration.py to set these values yourself
myColors = [[37,153,40,62,255,121], #Green
            [96,216,163,101,255,255], #Blue
            [112,89,162,169,255,299], #Purple
            [10,255,91,29,255,182]] #Yellow
myColorsBGR = [(0,255,127), #Green
               (255,0,0), #Blue
               (203,192,255), #Purple
               (255,255,0)] #Yellow

myPoints = [] #[[x,y,colorID]]

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPts = []

    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper) #color that you want as white and everything else as white
        x,y = findContours(mask)

        cv2.circle(imgResult,(x,y),10,myColorsBGR[count],cv2.FILLED)

        if x != 0 and y != 0:
            newPts.append([x,y,count])
        count += 1

    return newPts

def findContours(img):
    contours, hierarchy = cv2.findContours(img,mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_NONE)

    x,y,w,h = 0,0,0,0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500: #reduce noise and add drawing
            cv2.drawContours(imgResult, cnt, contourIdx=-1, color=(255, 0, 0), thickness=3)
            peri = cv2.arcLength(curve=cnt,closed=True)
            approxCorners = cv2.approxPolyDP(curve=cnt,epsilon=0.02*peri,closed=True)
            x, y, w, h = cv2.boundingRect(array=approxCorners) #create bounding box

    return (x+w//2),y

def drawOnCanvas(myPts,myColorsBGR):
    for point in myPts:
        cv2.circle(imgResult,center=(point[0],point[1]),radius=10,color=myColorsBGR[point[2]],thickness=cv2.FILLED)

## Cap import
cap = cv2.VideoCapture(0)
cap.set(3, FRAME_WIDTH)
cap.set(4, FRAME_HEIGHT)
cap.set(propId=10,value=150) #brightness

while True:
    isValid, img = cap.read()
    imgResult = img.copy()

    newPts = findColor(img, myColors)

    if len(newPts) != 0:
        for points in newPts:
            myPoints.append(points)

    if len(myPoints) != 0:
        drawOnCanvas(myPoints,myColorsBGR)

    cv2.imshow("virtualPaint (press 'q' to exit)", imgResult)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

