import time
import CameraServoWrapper as SERVO

smallServo = SERVO.CameraServoWrapper()
smallServo.setRawAngle(90)
time.sleep(5)
smallServo.upAngle(10)
time.sleep(2)
smallServo.upAngle(10)
