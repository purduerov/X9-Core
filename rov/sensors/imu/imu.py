from math import sin, pi


class IMU(object):
    """Mock IMU class
    """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.pitch = 0
        self.roll = 0
        self.yaw = 0

        self._angle = 0

    def read(self):
        self._angle += 1
        self.roll = sin(self._angle * (pi)/180.0)

    @property
    def data(self):
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "roll": self.roll,
            "pitch": self.pitch,
            "yaw": self.yaw
        }
