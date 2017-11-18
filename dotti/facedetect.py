#!/usr/bin/env python2.7

from picamera.array import PiRGBArray
from picamera import PiCamera
from dotti import Dotti
import cv2, time, sys, select


with Dotti('5C:31:3E:89:8F:F2', None, True) as dotti:
    dotti.setColor(black)
    
    #Load a cascade file for detecting faces
    face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
    #Get the picture (low resolution, so it should be quite fast)
    resolution = (320, 240)

    print("Press {enter} to exit")
    
    with PiCamera(resolution=resolution, framerate=32) as camera:
        rawCapture = PiRGBArray(camera, size=resolution)
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            #Convert to grayscale
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            #Look for faces in the image using the loaded cascade file
            faces = face_cascade.detectMultiScale(gray, 1.1, 5)
            #Truncate the stream for next iteration
            rawCapture.truncate(0)

            #Dotti logic to display the icon 
            if len(faces) > 0:                
                dotti.setIcon(2)
            else:
                dotti.setColor((0,0,0))

            print("[{}] Found {} face(s)".format(time.strftime("%X"), len(faces)))

            #Delay the next iteration
            time.sleep(1)

            #Enter key to exit loop
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                line = raw_input()
                break
