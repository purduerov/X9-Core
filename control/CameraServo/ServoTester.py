import time
import CameraServoWrapper as servo

smallServo = servo.Servo()
smallServo.setRawAngle(90)
time.sleep(5)
smallServo.upAngle(10)
time.sleep(2)
smallServo.upAngle(10)
