import smbus
import time

#Get I2C bus


class MS5837(object):
{
    #possibly have an address parameter to replace 0x76
    def __init__(self):
	self.bus = smbus.SMBus(1)
	self.address = 0x76
        self.bus.write_byte(self.address, 0x1E)
        #time.sleep(0.5)

    def read_pressure_sensitivity(self):
        data = self.bus.read_i2c_block_data(self.address, 0xA2, 2)
        return (data[0] * 256 + data[1])

    def read_pressure_offset(self):
        data = self.bus.read_i2c_block_data(self.address, 0xA4, 2)
        return (data[0] * 256 + data[1])

    def read_temp_coefficient_ofPressure(self):
        data = self.bus.read_i2c_block_data(self.address, 0xA6, 2)
        return (data[0] * 256 + data[1])

    def read_temp_reference(self):
        data = self.bus.read_i2c_block_data(self.address, 0xA8, 2)
        return (data[0] * 256 + data[1])

    def read_temp_coefficient_ofTemp(self):
        data = self.bus.read_i2c_block_data(self.address, 0xAC, 2)
        return (data[0] * 256 + data[1])

    def read_digital_pressure(self):
        # MS5837_30BA01 address, 0x76(118)
        #		0x40(64)	Pressure conversion(OSR = 256) command

        self.bus.write_byte(self.address, 0x40)
        #time.sleep(0.5)
        value = self.bus.read_i2c_block_data(self.address, 0x00, 3)
        return (value[0] * 65536 + value[1] * 256 + value[2])

        #QUESTION: Do I need to write_byte multiple times (I think so)

    def read_digital_temp(self):
        # MS5837_30BA01 address, 0x76(118)
        #		0x50(64)	Temperature conversion(OSR = 256) command
        self.bus.write_byte(self.address, 0x50)
        #time.sleep(0.5)
        value = self.bus.read_i2c_block_data(self.address, 0x00, 3)
        return (value[0] * 65536 + value[1] * 256 + value[2])


    def getPressure(self):
        C1 = self.read_pressure_sensitivity()
        C2 = self.read_pressure_offset()
        C3 = self.read_temp_coefficient()
        C4 = self.read_temp_reference()
        D1 = self.read_digital_pressure()

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

        return pressure
}
