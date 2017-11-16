from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time

#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

print("Press {enter} to exit")

#Get the picture (low resolution, so it should be quite fast)
with PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 32    
    rawCapture = PiRGBArray(camera, size=(640, 480))
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        #Convert to grayscale
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        #Look for faces in the image using the loaded cascade file
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        if len(faces) > 0:
            print "Found "+str(len(faces))+" face(s)"
        rawCapture.truncate(0)
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = raw_input()
            break


