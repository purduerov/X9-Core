from Adafruit_BNO055 import BNO055
import logging
import sys
import time

# Create and configure the BNO sensor connection.  Make sure only ONE of the
# below 'bno = ...' lines is uncommented:
# Raspberry Pi configuration with serial UART and RST connected to GPIO 18:



# BeagleBone Black configuration with default I2C connection (SCL=P9_19, SDA=P9_20),
# and RST connected to pin P9_12:
# bno = BNO055.BNO055(rst='P9_12')

# if not bno.begin():
#   raise RuntimeError('Failed to initialize BNO055! Check the Sensor DUMBASS')

class IMU(object):
    def __init__(self):
        bno.begin()
        bno = BNO055.BNO055(rst=18)

    def imu_get_data(self):

        heading, roll, pitch = bno.read_euler()
        gyro_x, gyro_y, gyro_z = bno.read_gyroscope()
        accel_x, accel_y, accel_z = bno.read_accelerometer()
        LinAccel_x, LinAccel_y, LinAccel_z = bno.read_linear_accelerometer()
        temp = bno.read_temp()
        return {'Heading': heading, 'Roll': roll, 'Pitch': pitch, 'Gyro-X': gyro_x, 'Gyro-Y': gyro_y, 'Gyro-Z': gyro_z,
                'Acceleration-X': accel_x, 'Acceleration-Y': accel_y, 'Acceleration-Z': accel_z,
                'Linear Acceleration-X': LinAccel_x, 'Linear Acceleration-Y': LinAccel_y, 'Linear Acceleration-Z': LinAccel_z,
                'Temp' : temp}

    def get_calibration(self):
        cal_array = bno.get_calibration()
        return cal_array

    def reset_calibration(self):
        cal_array_original = self.get_calibration()
        bno.set_calibration(bno.get_calibration())
        return cal_array_original

    def set_calibration(self, data):
        bno.set_calibration(data)
        return

    def sitrep (self):
        sys, gyro, accel, mag = bno.get_calibration_status()
        sys_stat, sys_test, sys_err = bno.get_system_status(True)
        good_status = [3,3,3,3,1,0x0F,0]
        test_array = [sys,gyro,accel,mag,sys_stat, sys_test, sys_err]

        for x in range(0, 4):
            if test_array[x] != 3:
                return False

        if test_array[4] == 1:
            return False

        if test_array[5] != 0x0F:
            return False

        if test_array[6] != 0:
            return False

        return True
