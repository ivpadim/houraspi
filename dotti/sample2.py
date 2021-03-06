#!/usr/bin/env python2.7

import sys, select, os, time, random
import bluepy
import bluepy.btle as btle
from dotti import Dotti

black = (0,0,0)

if __name__ == '__main__':
    device_addr = '5C:31:3E:89:8F:F2'
    if len(sys.argv) > 1:
        device_addr = sys.argv[1]
    
    dotti = Dotti(device_addr)
    dotti.connect() 
    
    print("Connected to device: {}".format(device_addr))
    print("Sample 2 running")
    dotti.setColor(black)
    for n in range(4):
        for pixel in range(64):
            red = random.randrange(255 if n == 1 else (1 * (pixel + 1)))
            green = random.randrange(255 if n ==2 else (1 * (pixel + 1)))
            blue = random.randrange(255 if n ==3 else (1 * (pixel + 1)))
            color = (red, green, blue)
            dotti.setPixelColor(pixel+1, color) 
            time.sleep(0.05)
    dotti.disconnect()
    print("Disconnected from device")
    print("Goodbye!")
    exit()
