from Adafruit_BNO055 import IMU as Adafruit_BNO055
from IMU_Mock import IMU as IMU_Mock

# Attemps to initialize the SparkFun IMU.
# If it fails on init, then use the mock IMU

def IMU():
    try:
        return Adafruit_BNO055()
    except Exception:
        print "Failed to Initialize Sparkfun IMU"
        print "Using Mock IMU"
        return IMU_Mock()
