from picamera.array import PiRGBArray
from picamera import PiCamera
from fractions import Fraction
import cv2
import time, sys, select

#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')

print("Press {enter} to exit")

resolution = (640, 480)
#Get the picture (low resolution, so it should be quite fast)
with PiCamera(
        resolution = resolution,
        framerate = Fraction(1, 6)
        ) as camera:
    rawCapture = PiRGBArray(camera, size=resolution)
    for frame in camera.capture_continuous(rawCapture,"bgr", use_video_port=True):
        image = frame.array
        #Convert to grayscale
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        #Look for faces in the image using the loaded cascade file
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        print("[{}] Found {} face(s)".format(time.strftime("%X"), len(faces)))
        rawCapture.truncate(0)
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = raw_input()
            break


