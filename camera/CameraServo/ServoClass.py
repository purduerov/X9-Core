import time
import wiringpi

class Servo(object):
  def __init__(self, pin=18):
    self.pin = pin
    #wiringpi.wiringPiSetupGPIO()
    #set the 18 pin to the a PWM output
    #NOTE: I am editing in github directly from a different computer...-_-
    #wiringpi.pinMode(self.pin, wiringpi.GPIO.PWM_OUTPUT)
    #set the PWM mode to milliseconds stype
    #wiringpi.pwmSetMode(wiringPi.GPIO.PWM_MODE_MS)
    #divide down the clock
    #wiringpi.pwmSetClock(192)
    #wiringpi.pwmSetRange(2000)

  def setAngle(self, angle):
    pulse = ((angle/180)+1)
    wiringpi.pwmWrite(self.pin, pulse)
