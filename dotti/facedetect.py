from picamera.array import PiRGBArray
from picamera import PiCamera
from fractions import Fraction
from dotti import Dotti
import cv2
import time, sys, select

#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')

print("Press {enter} to exit")

resolution = (640, 480)
black = (0,0,0)
no_faces_count = 0
icon_on = False

with Dotti('5C:31:3E:89:8F:F2', None, True) as dotti:
    #Get the picture (low resolution, so it should be quite fast)
    dotti.setColor(black)
    with PiCamera() as camera:
        camera.resolution = resolution
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=resolution)
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            #Convert to grayscale
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            #Look for faces in the image using the loaded cascade file
            faces = face_cascade.detectMultiScale(gray, 1.1, 5)
            if len(faces) > 0:
                print("[{}] Found {} face(s)".format(time.strftime("%X"), len(faces)))                
                no_faces_count = 0
                if not icon_on:
                    icon_on = True
                    dotti.setIcon(2)
            else:
                no_faces_count += 1
            if no_faces_count > 10:
                icon_on = False
                dotti.setColor(black)

            rawCapture.truncate(0)
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                line = raw_input()
                break


