import numpy as np
import matrixmaker


class ThrustMapper(object):
    """Class to be used to generate the desired thrust map based on the current and desired position"""
    """center is always (0, 0, 0) at center of mass"""
    # all trusters are assumed to be equidistant from the center of mass, with distance equal to 1
    # used to determine rotation about z (up/down) axis
    # these values work when thrusters are equidistant from center of mass
    """Thruster Locations (These are temp values for testing)
    Thruster 1 (3, -1.5, 0)
    Thruster 2 (3, 1, 0)
    Thruster 3 (-2, -1.5, 0)
    Thruster 4 (-2, 1, 0)
    Thruster 5 (1.5, -1, 1)
    Thruster 6 (1.5, 0.5, 1)
    Thruster 7 (-1, -1, 1)
    Thruster 8 (-1, 0.5, 1)
    """
    def __init__(self):
        self.thrustMap = np.array([0, 0, 0, 0, 0, 0])   # list for values that need to be output to the thrusters
        self.maker = matrixmaker.MatrixMaker(3, -1.5, 0, 3, 1, 0,
                                             -2, -1.5, 0, -2, 1, 0,
                                             1.5, -1, 1, 1.5, 0.5, 1,
                                             -1, -1, 1, -1, 0.5, 1)
        self.mutationMatrix = self.maker.generate_matrix()

    def generate_thrust_map(self, desired):
        """generate the thrustMap to move to the desired vector

        desired (Vector6)
        """
        # some math to determine the thrustMap
        self.thrustMap = self.mutationMatrix.dot(desired)
        return self.thrustMap

