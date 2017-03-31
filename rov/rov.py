import copy
import os

from threading import Lock
from time import time, sleep


from sensors import Pressure, IMU
from camera.cam import Camera

from hardware.MotorControl import MotorControl

from thrusters.Control import ThrusterControl
from thrusters.hardware.PWM_Control import Thrusters
from thrusters.mapper.Simple import Mapper


class ROV(object):

    def __init__(self):
        self._data = {}
        self._control_data = {}
        self._new_data = False
        self._last_packet = time() - 1

        self.last_update = time()
        self.last_print = time()

        self._running = True

        self._data_lock = Lock()

        self._control_data_lock = Lock()

        self.debug = (os.environ.get("ROV_DEBUG") == "1")

        self.init_hw()

    def init_hw(self):
        self.camera1 = Camera()
        self.camera1.on()

        self.motor_control = MotorControl(
            zero_power=310,
            neg_max_power=227,
            pos_max_power=393,
            frequency=47
        )

        self.thrusters = Thrusters(
            self.motor_control,
            [6, 1, 4, 3, 5, 12, 8, 9]
        )

        self.thrust_mapper = Mapper()

        self.thruster_control = ThrusterControl(
            self.thrusters,
            self.mapper,
            num_thrusters=8,
            ramp=True,
            max_ramp=0.05
        )

        self.update_objects = {
            "imu": IMU(),
            "pressure": Pressure(),
            "thrusters": self.thruster_control
        }

    @property
    def data(self):
        with self._data_lock:
            return copy.deepcopy(self._data)

    @property
    def control_data(self):
        with self._control_data_lock:
            return self._control_data

    @control_data.setter
    def control_data(self, val):
        with self._control_data_lock:
            self._control_data = copy.deepcopy(val)
            self._new_data = True
            self._last_packet = time()

    def debug_print(self):
        if time() - self.last_print > 0.4:
            print '\n\nControl Data: '
            print self.control_data

            print '\n\nROV Data: '
            print self._data

            self.last_print = time()

    def update(self):
        with self._data_lock:
            if self._new_data:
                self._new_data = False
            elif time() - self._last_packet > 0.5:
                print 'Data connection lost'
                self.thruster_control.stop()

            control_data = self.control_data

            # Update all objects and copy over their data
            for obj in self.update_objects:
                # The control_data['obj_name'] data gets unpacked and directly
                # passed into the update methods as arguments
                try:
                    self.update_objects[obj].update(**control_data[obj])
                    self._data[obj] = self.update_objects[obj].data
                except Exception as e:
                    print "Failed updating: %s" % obj
                    print e.message

            # Our last update
            self.last_update = time()

            if self.debug:
                self.debug_print()

    def run(self):
        while self._running:
            while time() - self.last_update < 0.01:
                sleep(0.005)

            try:
                self.update()
            except Exception as e:
                print e.message

if __name__ == "__main__":
    r = ROV()
    r.run()
