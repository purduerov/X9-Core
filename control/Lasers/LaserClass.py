import wiringpi

class Laser(object):
    def __init__(self, pin=None):
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(pin, wiringpi.GPIO.OUTPUT)
        self._pin = pin

    def turnOn(self):
        wiringpi.digitalWrite(self._pin, 1)

    def turnOff(self):
        wiringpi.digitalWrite(self._pin, 0)

    def cleanUp(self):
        wiringpi.digitalWrite(self._pin, 0)
        wiringpi.pinMode(self._pin, wiringpi.GPIO.INPUT)

    def resetPin(self, pin):
        self.cleanUp()
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(pin, wiringpi.GPIO.OUTPUT)
        self._pin = pin
        