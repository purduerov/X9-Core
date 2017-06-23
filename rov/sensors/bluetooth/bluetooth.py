import serial


class Bluetooth(object):

    def __init__(self):
        self.bluetooth_serial = serial.Serial()
        self.bluetooth_serial.open()

    def read(self):
        res = ''
        i = 7
        while self.bluetooth_serial.in_waiting and i != 0:
            res = res + self.bluetooth_serial.read()
            i += 1
        res += "\n"
        return res


if __name__ == "__main__":
    bluetooth = Bluetooth()
    while True:
        print bluetooth.read()
