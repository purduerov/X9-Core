import time
import wiringpi
import ServoClass as Servo
from CameraServoWrapper import CameraServoWrapper as ServoWrapper

wiringpi.wiringPiSetupGPIO()
smallServo = ServoWrapper(pin=18)
smallServo.setRawAngle(45)
time.sleep(5)
smallServo.upAngle(10)
time.sleep(2)
smallServo.upAngle(10)
time.sleep(2)
smallServo.upAngle(90)
time.sleep(2)
smallServo.positionAtZero()
time.sleep(2)
smallServo.setHomeToCurrentAngle()
smallServo.setRawAngle(180)
time.sleep(2)
smallServo.positionAtHome()

