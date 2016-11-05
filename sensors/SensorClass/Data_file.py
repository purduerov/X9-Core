import logging
import sys
import time
import SensorClasses


class State(object):
    def __init__(self):
        self.imu = SensorClasses.IMU()
        self.pressure = SensorClasses.Pressure()

    def get_state(self, state_value):
        # gets the data from the corresponding classes and appends it to the main dictionary
        main_dict = self.imu.imu_get_data()
	if state_value == ('Pressure' or 'cTemp' or 'fTemp'):
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
