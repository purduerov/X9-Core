import copy
import os
import traceback

from threading import Lock
from time import time, sleep


from sensors import Pressure, IMU
from camera import Cameras

from hardware.motor_control import MotorControl

from thrusters.Control import ThrusterControl
from thrusters.hardware.PWM_Control import Thrusters
from thrusters.mapper.Simple import Mapper

from tools import Claw, ValveTurner


class ROV(object):

    def __init__(self, lock, data):
        self._data_lock = lock
        self._data = data

        self._control_data = {}
        self._new_data = False
        self._last_packet = time() - 1

        self.last_update = time()
        self.last_print = time()

        self._running = True

        self._control_data_lock = Lock()

        self.debug = (os.environ.get("ROV_DEBUG") == "1")

        self.init_hw()

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

    def run(self):
        while self._running:
            while time() - self.last_update < 0.01:
                sleep(0.005)

            try:
                self.update()
            except Exception as e:
                print "Exception: %s" % e
                print traceback.format_exc()

    def init_hw(self):
        self.cameras = Cameras(
            resolution='1280x720',
            framerate=30,
            port_start=8080,
            brightness=16,
            contrast=32
        )

        self.motor_control = MotorControl(
            zero_power=305,
            neg_max_power=222,
            pos_max_power=388,
            frequency=47
        )

        self.thrusters = Thrusters(
            self.motor_control,
            [7, 4, 6, 5, 10, 0, 11, 1]
        )

        self.thrust_mapper = Mapper()

        self.thruster_control = ThrusterControl(
            self.thrusters,
            self.thrust_mapper,
            num_thrusters=8,
            ramp=True,
            max_ramp=0.05
        )

        self.claw = Claw(
            self.motor_control,
            pin=3
        )

        self.valve_turner = ValveTurner(
            self.motor_control,
            pin=9
        )

        self.IMU = IMU()

        self.pressure = Pressure()

    def update(self):
        with self._data_lock:
            if self._new_data:
                self._new_data = False
            elif time() - self._last_packet > 0.5:
                print 'Data connection lost'
                self.motor_control.kill()
                self.thruster_control.stop()

            control_data = self.control_data

            try:
                self.thruster_control.update(**control_data['thrusters'])
                self.claw.manipulate(**control_data['claw'])
                self.valve_turner.manipulate(**control_data['valve_turner'])

                self.pressure.update()
                self.IMU.update()

            except Exception as e:
                print "Failed updating things"
                print "Exception: %s" % e
                print traceback.format_exc()

            # Our last update
            self.last_update = time()

            if self.debug:
                self.debug_print()
