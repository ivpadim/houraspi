#!/usr/bin/env python2.7

import sys, select, os, time, struct, random
import bluepy
import bluepy.btle as btle

class Dotti():
    def __init__(self, device_addr, address_type=None):
        self.device_addr  = device_addr
        if not address_type:
            address_type = btle.ADDR_TYPE_PUBLIC
        self.address_type = address_type

    def connect(self):
        self.connection = btle.Peripheral(self.device_addr, self.address_type)
        self.command    = btle.Characteristic(self.connection, btle.UUID('fff3'), 0x29, 8, 0x2A)

    def disconnect(self):
        self.connection.disconnect()

    def setPixelColor(self, pixel, red, green, blue):
        self.command.write(struct.pack('<BBBBBB', 0x07, 0x02, pixel+1, red, green, blue))

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
        dotti.setPixelColor(pixel+1, red, green, blue)
        time.sleep(0.1)

        #Turn off random led pixel
        pixel = random.randrange(64)
        dotti.setPixelColor(pixel+1, 0x00, 0x00, 0x00)
        time.sleep(0.1)
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = raw_input()
            break
    dotti.disconnect()
    print("Disconnected from device")
    print("Goodbye!")
    exit()
