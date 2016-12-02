#import time
import wiringpi

class Servo(object):
    def __init__(self):
        wiringpi.wiringPiSetupGpio()
        #set the 18 pin to the a PWM output
        wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
        #set the PWM mode to milliseconds stype
        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
        #divide down the clock
        wiringpi.pwmSetClock(192)
        wiringpi.pwmSetRange(2000)

    def setAngle(self, angle):
        pulse = ((angle/180)+1)
        wiringpi.pwmWrite(18, pulse)
        
