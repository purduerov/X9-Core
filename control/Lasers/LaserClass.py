import wiringpi



class Laser(object):
    def __init__(self, pin=None):
        self._pin = pin
# BMAX:TODO: WARN: See the Servo library comments...
        #wiringpi.wiringPiSetupGpio()
# BMAX:TODO: INFO: You did right on pin parameters this time!
        wiringpi.pinMode(pin, wiringpi.GPIO.OUTPUT)
# BMAX:TODO: WARN: Just a code style notice. Its good practice to assign parameters to instance variables BEFORE either the parameter or the instance variable is used in any functions (as above line). This removes any possiblity of confusion on which variable is being accessed by the function, since oftentimes the instance variable and the parameter variable are called the same thing, even though that isn't quite the case here.
        #self._pin = pin

    def turnOn(self):
        wiringpi.digitalWrite(self._pin, 0)

    def turnOff(self):
        wiringpi.digitalWrite(self._pin, 1)

    def cleanUp(self):
        wiringpi.digitalWrite(self._pin, 0)
        wiringpi.pinMode(self._pin, wiringpi.GPIO.INPUT)

    def resetPin(self, pin):
        self.cleanUp()
        self._pin = pin
# BMAX:TODO: WARN: See the Servo library comments...
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(pin, wiringpi.GPIO.OUTPUT)
# BMAX:TODO: WARN: see above warning, this function is essentially performing all the same operations as constructor, so it should be held to same standards. move ^^^.
        #self._pin = pin

