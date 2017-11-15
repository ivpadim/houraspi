#!/usr/bin/env python2.7

import sys, select, os, time, random
import bluepy
import bluepy.btle as btle
from dotti import Dotti

if __name__ == '__main__':
    device_addr = '5C:31:3E:89:8F:F2'
    if len(sys.argv) > 1:
        device_addr = sys.argv[1]
    
    with Dotti(device_addr, None, True) as dotti:
        print("Connected to device: {}".format(device_addr))
        print("Sample 3 running")
        black = (0,0,0)
        dotti.setColor(black)
        for n in range(5):
            red = random.randrange(256)
            green = random.randrange(256)
            blue = random.randrange(256)
            color = (red, green, blue)
            for pixel in range(64):
                dotti.setPixelColor(pixel + 1, color)
                time.sleep(0.05)
    print("Disconnected from device")
    print("Goodbye!")
    exit()
