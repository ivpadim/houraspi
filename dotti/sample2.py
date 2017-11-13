#!/usr/bin/env python2.7

import sys, select, os, time, random
import bluepy
import bluepy.btle as btle
from dotti import Dotti

if __name__ == '__main__':
    device_addr = '5C:31:3E:89:8F:F2'
    if len(sys.argv) > 1:
        device_addr = sys.argv[1]
    
    dotti = Dotti(device_addr)
    dotti.connect() 
    
    print("Connected to device: {}".format(device_addr))
    print("Sample 2 running")
    dotti.setColor(0,0,0)
    for n in range(3):
        for pixel in range(64):
            red = random.randrange((pixel+1)*4)
            green = random.randrange((pixel+1)*4)
            blue = random.randrange((pixel+1)*4)
            dotti.setPixelColor(pixel+1, red, green, blue) 
            time.sleep(0.05)
    dotti.disconnect()
    print("Disconnected from device")
    print("Goodbye!")
    exit()
