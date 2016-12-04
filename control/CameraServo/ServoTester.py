import time
import ServoClass as Servo
from CameraServoWrapper import CameraServoWrapper as ServoWrapper

smallServo = ServoWrapper()
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

