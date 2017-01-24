import sys
sys.path.append('./sensors/sensorLibs/Adafruit_Python_BNO055-master/Adafruit_BNO055')
import BNO055

import logging
import sys
import time
from smbus import SMBus

# Create and configure the BNO sensor connection.  Make sure only ONE of the
# below 'bno = ...' lines is uncommented:
# Raspberry Pi configuration with serial UART and RST connected to GPIO 18:





# if not bno.begin():
#   raise RuntimeError('Failed to initialize BNO055! Check the Sensor DUMBASS')

class IMU(object):
    def __init__(self):
        self.bno = BNO055.BNO055(rst=18)
        self.bno.begin()


    def imu_get_data(self):

        heading, roll, pitch = self.bno.read_euler()
        gyro_x, gyro_y, gyro_z = self.bno.read_gyroscope()
        accel_x, accel_y, accel_z = self.bno.read_accelerometer()
        LinAccel_x, LinAccel_y, LinAccel_z = self.bno.read_linear_acceleration()
        temp = self.bno.read_temp()
        return {'Heading': heading, 'Roll': roll, 'Pitch': pitch, 'Gyro-X': gyro_x, 'Gyro-Y': gyro_y, 'Gyro-Z': gyro_z,
                'Acceleration-X': accel_x, 'Acceleration-Y': accel_y, 'Acceleration-Z': accel_z,
                'Linear Acceleration-X': LinAccel_x, 'Linear Acceleration-Y': LinAccel_y, 'Linear Acceleration-Z': LinAccel_z,
                'Temp' : temp}

    def get_calibration(self):
        cal_array = self.bno.get_calibration()
        return cal_array

    def reset_calibration(self):
        cal_array_original = self.get_calibration()
        self.bno.set_calibration(self.bno.get_calibration())
        return cal_array_original

    def set_calibration(self, data):
        self.bno.set_calibration(data)
        return

    def sitrep (self):
        sys, gyro, accel, mag = self.bno.get_calibration_status()
        sys_stat, sys_test, sys_err = self.bno.get_system_status(True)
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


class Pressure(object):

    def __init__(self):
        self.bus = smbus.SMBus(1)

    def get_pressure(self):
        self.bus.write_byte(0x76, 0x1E)
#time.sleep(.5)
        # Read 12 bytes of calibration data
        # Read pressure sensitivity
        data = self.bus.read_i2c_block_data(0x76, 0xA2, 2)
        C1 = data[0] * 256 + data[1]

        # Read pressure offset
        data = self.bus.read_i2c_block_data(0x76, 0xA4, 2)
        C2 = data[0] * 256 + data[1]

        # Read temperature coefficient of pressure sensitivity
        data = self.bus.read_i2c_block_data(0x76, 0xA6, 2)
        C3 = data[0] * 256 + data[1]

        # Read temperature coefficient of pressure offset
        data = self.bus.read_i2c_block_data(0x76, 0xA8, 2)
        C4 = data[0] * 256 + data[1]

        # Read reference temperature
        data = self.bus.read_i2c_block_data(0x76, 0xAA, 2)
        C5 = data[0] * 256 + data[1]

        # Read temperature coefficient of the temperature
        data = self.bus.read_i2c_block_data(0x76, 0xAC, 2)
        C6 = data[0] * 256 + data[1]

        # MS5837_30BA01 address, 0x76(118)
        #		0x40(64)	Pressure conversion(OSR = 256) command
        self.bus.write_byte(0x76, 0x40)

        time.sleep(0.5)

        # Read digital pressure value
        # Read data back from 0x00(0), 3 bytes
        # D1 MSB2, D1 MSB1, D1 LSB
        value = self.bus.read_i2c_block_data(0x76, 0x00, 3)
        D1 = value[0] * 65536 + value[1] * 256 + value[2]

        # MS5837_30BA01 address, 0x76(118)
        #		0x50(64)	Temperature conversion(OSR = 256) command
        self.bus.write_byte(0x76, 0x50)

        time.sleep(0.5)

        # Read digital temperature value
        # Read data back from 0x00(0), 3 bytes
        # D2 MSB2, D2 MSB1, D2 LSB
        value = self.bus.read_i2c_block_data(0x76, 0x00, 3)
        D2 = value[0] * 65536 + value[1] * 256 + value[2]

        dT = D2 - C5 * 256
        TEMP = 2000 + dT * C6 / 8388608
        OFF = C2 * 65536 + (C4 * dT) / 128
        SENS = C1 * 32768 + (C3 * dT ) / 256
        T2 = 0
        OFF2 = 0
        SENS2 = 0

        if TEMP >= 2000 :
                T2 = 2 * (dT * dT) / 137438953472
                OFF2 = ((TEMP - 2000) * (TEMP - 2000)) / 16
                SENS2 = 0
        elif TEMP < 2000 :
                T2 = 3 *(dT * dT) / 8589934592
                OFF2 = 3 * ((TEMP - 2000) * (TEMP - 2000)) / 2
                SENS2 = 5 * ((TEMP - 2000) * (TEMP - 2000)) / 8
                if TEMP < -1500 :
                    OFF2 = OFF2 + 7 * ((TEMP + 1500) * (TEMP + 1500))
                    SENS2 = SENS2 + 4 * ((TEMP + 1500) * (TEMP + 1500))

        TEMP = TEMP - T2
        OFF2 = OFF - OFF2
        SENS2 = SENS - SENS2
        pressure = ((((D1 * SENS2) / 2097152) - OFF2) / 8192) / 10.0
        cTemp = TEMP / 100.0
        fTemp = cTemp * 1.8 + 32

        return { "mbar": pressure, "cTemp": cTemp, "fTemp": fTemp }



if __name__ == "__main__":
        test = IMU()
        test2 = Pressure()
        while True :
                testdict = test.imu_get_data()
                testarray = test2.get_pressure()
                print( testdict['Heading'] )
                print(testdict['Roll'])
                print(testarray[0])
                time.sleep(1)
