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
    print("Random coloring sequence")
    print("Press enter to exit")
    while True:

        #Turn on random led pixel
        pixel = random.randrange(64)
        red   = random.randrange(256)
        green = random.randrange(256)
        blue  = random.randrange(256)
        color = (red, green, blue)
        dotti.setPixelColor(pixel+1, color)
        time.sleep(0.05)

        #Turn off random led pixel
        pixel = random.randrange(64)
        dotti.setPixelColor(pixel+1, (0, 0, 0))
        time.sleep(0.05)
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = raw_input()
            break

    dotti.disconnect()

    print("Disconnected from device")
    print("Goodbye!")
    exit()
