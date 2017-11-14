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
    print("Sample 4 running")
    dotti.setColor(0,0,0)
    for n in range(3):
        dotti.setIcon(5)
        time.sleep(1)
        dotti.setColor(0,0,0)
        time.sleep(1)

    dotti.disconnect()
    print("Disconnected from device")
    print("Goodbye!")
    exit()
