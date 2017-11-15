#!/usr/bin/env python2.7

import sys
import picamera
import time
from dotti import Dotti

if __name__ == '__main__':
    device_addr = '5C:31:3E:89:8F:F2'
    output = "image.jpg"
    if len(sys.argv) > 1:
        device_addr = sys.argv[1]
    if len(sys.argv) > 2:
        output = sys.argv[2]
    
    #setup the connection to dotti
    with Dotti(device_addr, None, True) as dotti:
        print("Taking picture")
        dotti.setColor((255,255,255))
        time.sleep(0.1)
        with picamera.PiCamera() as camera:            
            camera.resolution = (1280,720)
            camera.capture(output)
        time.sleep(0.5)
        dotti.setColor((0,0,0))

    print("Goodbye!")
    exit()
