from picamera import PiCamera
from fractions import Fraction
import cognitive_face as cf
import sys, select, io
from azure_keys import *

cf.Key.set(face_api_key)
cf.BaseUrl.set(face_api_url)

resolution = (640, 480)
count = 1

print("Press {enter} to exit")
#Get the picture (low resolution, so it should be quite fast)
#For low light: Uncomment the framerate, sensor mode, shutter speed, iso and exposure_mode 
with PiCamera(
        resolution = resolution,
        #framerate = Fraction(1,2),
        #sensor_mode = 3
        ) as camera:
    #camera.shutter_speed = 4000000
    #camera.iso = 800
    #camera.exposure_mode = 'off'
    stream = io.BytesIO()
    for frame in camera.capture_continuous(stream, "jpeg",quality=100):
        stream.seek(0)
        result = cf.face.detect(stream)
        print(result)
        #debugging write the image to disk
        #with open('{}.jpg'.format(count), 'w') as img:
        #    img.write(stream.read())
        #count += 1
        stream.seek(0)
        stream.truncate()
        #enter to exit logic
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = raw_input()
            break


