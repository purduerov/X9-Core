import wiringpi

class Led(object):

    def __init__(self, pin=16, setupWiringPi=True):
        self.pin = pin

        # sets up wiring pi gpio
        if setupWiringPi:
            wiringpi.wiringPiSetupGpio()

        # set the pin to pwm output
        wiringpi.pinMode(self.pin, wiringpi.OUTPUT)
        self.off()

    def write(self, value):
        if value != 0:
            value = 1

        wiringpi.digitalWrite(self.pin, value)

    def on(self):
        self.write(0)

    def off(self):
        self.write(1)
