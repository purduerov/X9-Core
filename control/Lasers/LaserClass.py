import wiringpi



class Laser(object):
    def __init__(self, pin=None):
        self._pin = pin
        #wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(self._pin, wiringpi.GPIO.OUTPUT)
        #self._pin = pin

    def turnOn(self):
        wiringpi.digitalWrite(self._pin, 0)

    def turnOff(self):
        wiringpi.digitalWrite(self._pin, 1)

    def __del__(self):
        wiringpi.digitalWrite(self._pin, 0)
        wiringpi.pinMode(self._pin, wiringpi.GPIO.INPUT)

