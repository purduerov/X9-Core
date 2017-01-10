import time
import wiringpi

class Servo(object):
  def __init__(self):
# BMAX:TODO: WARN: wiringpi is a class, not an object. If we have multiple servos, SHOULD we be calling setup multiple times? An option is to create a static variable to keep track if a Servo object has been created and thus wiringpi has been setup, but the BEST option is to find where the rov object is created (this object SHOULD only be created once) and have setup be called there. It may seem weird that we have to import the module twice, and you may wonder if the state of the module in ROV will be the same as in Servo, and the answer is yes according to python 2.7 standards. See https://docs.python.org/2/faq/programming.html last question's answer gives us the deets that a module imported already will just use that module's state. Other websites go into more detail and say that importing a module actually creates an object of that class (which makes sense, it has to in order to save state).
    wiringpi.wiringPiSetupGPIO()
    #set the 18 pin to the a PWM output
# BMAX:TODO: MAJOR: proper programming style teaches you should not hardcode values like this. We may only want to make one of these objects at the time, but WE MAY want to make more later... So have an instance variable for the pin, and request a parameter in the object (default value = 18 will be good, so you don't have to change implementation code) constructor.
    wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
    #set the PWM mode to milliseconds stype
    wiringpi.pwmSetMode(wiringPi.GPIO.PWM_MODE_MS)
    #divide down the clock
    wiringpi.pwmSetClock(192)
    wiringpi.pwmSetRange(2000)

  def setAngle(self, angle):
    pulse = ((angle/180)+1)
    wiringpi.pwmWrite(18, pulse)
