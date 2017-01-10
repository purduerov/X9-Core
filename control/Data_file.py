import logging
import sys
import time
import SensorClasses

# BMAX:TODO: MAJOR: I realize this class may work and be good for testing, but I need a folder of the IMU and Pressure classes that don't rely on integrating with this class, but rather integrate with how the actual ROV object will work. We can talk about this on Saturday, but essentially I need the classes returning dicts containing their sensor statuses only. Pressure is currently not compatible with this.

class State(object):
    def __init__(self):
        self.imu = SensorClasses.IMU()
        self.pressure = SensorClasses.Pressure()

    def get_state(self, state_value):
        # gets the data from the corresponding classes and appends it to the main dictionary
        main_dict = self.imu.imu_get_data()
	if state_value == ('Pressure' or 'cTemp' or 'fTemp' or 'all'):
		temp_array = self.pressure.get_pressure()
		main_dict['ctemp'] = temp_array[1]
        	main_dict['fTemp'] = temp_array[2]
		main_dict['Pressure'] = temp_array[0]
        # for the case of multiple arguments
        if state_value == 'all':
		return main_dict # reformat to an array that looks like the one charles gave you

        else:
		return main_dict.get(state_value)

if __name__ == '__main__':
    	test = State()

	while True:
        	print( test.get_state('Pressure'))
