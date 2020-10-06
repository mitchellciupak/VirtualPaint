import cv2
import numpy as np

# Macros
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

"""
Instructions:
    1. Hold desired color to camera
    2. Run colorCalibration.py
    2. Adjust the bars on TrackBars until all but the object holding the color is black
        - Note: It is best to get as tight of a bound as possible, so adjust bars as close to non-recognition as possible
    3. Copy down values like [HueMin, SatMin, ValMin, HueMax, SatMax, ValMax]
    4. Update each new color as an array to myColors in ./virtualPaint.py
    4. press 'q' to exit
    5. repeat for new colors
"""

def empty(arg):
    pass

def colorDetection(img):

    # Define color limits to identify with adjustable track bar
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars", 640, 240)
    cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
    cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
    cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
    cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
    cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
    cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

    while True:
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        hue_min = cv2.getTrackbarPos("Hue Min","TrackBars")
        hue_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
        sat_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
        sat_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
        val_min = cv2.getTrackbarPos("Val Min", "TrackBars")
        val_max = cv2.getTrackbarPos("Val Max", "TrackBars")

        #Color
        lower = np.array([hue_min,sat_min,val_min])
        upper = np.array([hue_max,sat_max,val_max])
        mask = cv2.inRange(imgHSV,lower,upper) #color that you want as white and everything else as white
        imgResults = cv2.bitwise_and(img,img,mask=mask)

        cv2.imshow("Mask (All black but the color)", mask)
        cv2.imshow("Results (Only color visable)", imgResults)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":

    #Read in first image from cap
    cap = cv2.VideoCapture(0)
    cap.set(3, FRAME_WIDTH)
    cap.set(4, FRAME_HEIGHT)
    cap.set(propId=10, value=150)  # brightness

    isValid, img = cap.read()

    colorDetection(img)

