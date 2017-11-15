#!/usr/bin/env python2.7

import sys, select, os, time, random
import bluepy
import bluepy.btle as btle
from dotti import Dotti

red   = (255,0,0)
green = (0,255,0)
raspi = { 2:green, 3:green, 6:green, 7:green,
          12:red, 13:red,
          19:red, 20:red, 22:red,
          26:red, 28:red, 29:red, 31:red,
          34:red, 35:red, 36:red, 37:red, 38:red, 39:red,
          42:red, 44:red, 45:red, 47:red,
          51:red, 53:red, 54:red,
          60:red, 61:red }


if __name__ == '__main__':
    device_addr = '5C:31:3E:89:8F:F2'
    if len(sys.argv) > 1:
        device_addr = sys.argv[1]
    
    with Dotti(device_addr, None, True) as dotti:
    
        print("Connected to device: {}".format(device_addr))
        print("Sample 5 running")
    
        dotti.setColor((0,0,0))

        for px, color in raspi.iteritems():
            dotti.setPixelColor(px, color)
            time.sleep(0.05)

    print("Disconnected from device")
    print("Goodbye!")
    exit()
