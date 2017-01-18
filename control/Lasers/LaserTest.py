from LaserCLass import Laser
import time
import wiringpi

wiringpi.wiringPiSetupGpio()
lsr = Laser(pin=15)
lsr.turnOn()
time.sleep(5)
lsr.turnOff()
time.sleep(5)
lsr.turnOn()
time.sleep(5)
lsr.turnOff()
