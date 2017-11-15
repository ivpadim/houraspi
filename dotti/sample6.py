#!/usr/bin/env python2.7

import sys, select, os, time, random
from dotti import Dotti

if __name__ == '__main__':
    device_addr = '5C:31:3E:89:8F:F2'
    if len(sys.argv) > 1:
        device_addr = sys.argv[1]
    
    dotti = Dotti(device_addr)
    dotti.connect() 
    
    print("Connected to device: {}".format(device_addr))
    print("Sample 6 running")
    print("Press enter to exit")
    dotti.setColor((0,0,0))

    while True:
        level = random.randrange(7)
        red = random.randrange(256)
        green = random.randrange(256)
        blue =random.randrange(256)
        dotti.setBarLevel(level + 1, (red, green, blue))
        delay = random.randrange(50)
        time.sleep(0.45 + (1/(delay + 1)))
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = raw_input()
            break

    dotti.disconnect()
    print("Disconnected from device")
    print("Goodbye!")
    exit()
