import struct
import bluepy
import bluepy.btle as btle

class Dotti():
    def __init__(self, device_addr, address_type=None):
        self.device_addr  = device_addr
        if not address_type:
            address_type  = btle.ADDR_TYPE_PUBLIC
        self.address_type = address_type

    def connect(self):
        self.connection = btle.Peripheral(self.device_addr, self.address_type)
        self.command    = btle.Characteristic(self.connection, btle.UUID('fff3'), 0x29, 8, 0x2A)

    def disconnect(self):
        self.connection.disconnect()

    def setPixelColor(self, pixel, red, green, blue):
        self.command.write(struct.pack('<BBBBBB', 0x07, 0x02, pixel, red, green, blue))

    def setColor(self, red, green, blue):
        self.command.write(struct.pack('<BBBBB', 0x06, 0x01, red, green, blue))

    def setBarLevel(self, level, red, green, blue):
        self.command.write(struct.pack('<BBBBBB', 0x07, 19, level, red, green, blue))

    def setIcon(self, index):
        if index == 1:
            self.command.write(struct.pack('<BBBii', 0x06, 0x08, 0x0, 0, 0))
        elif index == 2:
            self.command.write(struct.pack('<BBBi', 0x06, 0x08, 0x02, -112))
        elif index == 3:
            self.command.write(struct.pack('<BBBi', 0x06, 0x08, 0x02, -96))
        elif index == 4:
            self.command.write(struct.pack('<BBBi', 0x06, 0x08, 0x02, -80))
        elif index == 5:
            self.command.write(struct.pack('<BBBi', 0x06, 0x08, 0x02, -64))
        elif index == 6:
            self.command.write(struct.pack('<BBBi', 0x06, 0x08, 0x02, -48))
        elif index == 7:
            self.command.write(struct.pack('<BBBi', 0x06, 0x08, 0x02, -32))
        elif index == 8:
            self.command.write(struct.pack('<BBBi', 0x06, 0x08, 0x02, -16))
        else:
            print('Not available, try [1..8]')

