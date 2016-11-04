import logging
import sys
import time
import SensorClasses


class State(object):
    def __init__(self):
        self.imu = SensorClasses.IMU
        self.pressure = SensorClasses.Pressure

    def get_state(self, *args):
        state_value = []
        index = 0;

        # gets the data from the corresponding classes and appends it to the main dictionary
        main_dict = self.imu.imu_get_data()
        main_dict['Pressure'] = self.pressure.get_pressure[0]
        main_dict['ctemp'] = self.pressure.get_pressure[1]
        main_dict['fTemp'] = self.pressure.get_pressure[2]

        # for the case of multiple arguments
        for arg in args:
            state_value[index] = arg
            index += 1

        if state_value[0] == 'all':
            return main_dict # reformat to an array that looks like the one charles gave you

        elif len(args) == 1:
            return [main_dict.get(state_value[0])]

        else:
            output_array = []
            for x in range(0, index):
                output_array.append(main_dict.get(state_value[x]))
            return output_array

if __name__ == '__main__':
    test = State()

    while True:
        print("One arg: %d\n", test.get_state('heading')[0])
        time.sleep(2)
        print("multiple args: %d, %d, %d, \n" %(test.get_state('Roll', 'Pitch', 'Pressure')[0],test.get_state('Roll', 'Pitch', 'Pressure')[1],test.get_state('Roll', 'Pitch', 'Pressure')[2]))
        time.sleep(2)
        print("multiple args without extra function calls: ", test.get_state('Roll', 'Pitch', 'Pressure'))
        time.sleep(2)
        print("whole array: ", test.get_state('all'))