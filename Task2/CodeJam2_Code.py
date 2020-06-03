from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2

vs = cv2.VideoCapture("Downloads/sentry3.mkv")

# initialising the first frame in the video stream
firstFrame = None
min_area=2750
r=0
# looping over the frames of the video
while True:
    r+=1
    ret, frame = vs.read()
    # if the frame could not be accesses, we have reached the end of the video
    if frame is None:
        break
    # resizing the frame, converting to grayscale, and blurring it
    # frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (17, 17), 0)
    # if the first frame is None, initialise it
    if firstFrame is None:
        firstFrame = gray
        continue
    # computing the absolute difference between the current frame and first frame
    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    # dilating the thresholded image to fill in holes and then finding contours on thresholded image
    thresh = cv2.dilate(thresh, None, iterations=0)
    cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    t=0
    s=0
    m,n=0,0
    # looping over the contours
    # cv2.drawContours(frame,cnts,-1,(255,0,0),thickness=4)
    for c in cnts:
        s+=1
        # if the contour is too small, ignore it
        if cv2.contourArea(c) < 700 and cv2.contourArea(c)>160 and cv2.arcLength(c,True)>35+r/3:
            (x, y, w, h) = cv2.boundingRect(c)
            if r<=55:
                cv2.putText(frame, "Robot 2", (x-10,y+80), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)
            if r<130 and r > 55:
                if cv2.arcLength(c,True)> 62 + (r-40)/4:
                    cv2.putText(frame, "Robot 1", (x-10,y+50), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)
                else:
                    cv2.putText(frame, "Robot 2", (x-10,y+50), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)
                continue
            elif r>=130:
                if cv2.arcLength(c,True)>90+r/5:
                    cv2.putText(frame, "Robot 2", (x-10,y+50), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)
                else:
                    cv2.putText(frame, "Robot 1", (x-10,y+80), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)
                continue
        if cv2.contourArea(c) < min_area:
            continue
        t+=1
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)    
    cv2.imshow("Security Feed", frame)
    # cv2.imshow("Thresh", thresh)
    # cv2.imshow("Frame Delta", frameDelta)
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key is pressed, break from the lop
    if key == ord("q"):
        break
#closing any open windows

vs.release()
cv2.destroyAllWindows()