import numpy as np


class ThrustMapper(object):
    """Class to be used to generate the desired thrust map based on the current and desired position"""
    xComp = 0.2696336857
    yComp = 0.6673667906
    """center is always (0, 0, 0)"""
    # all trusters are assumed to be equidistant from the center of mass, with distance equal to 1
    # used to determine rotation about z (up/down) axis
    # these values work when thrusters are equidistant from center of mass
    """Thruster Locations (These are temp values for testing)
    Thruster 1 (1,-1)
    Thruster 2 (1, 1)
    Thruster 3 (-1, -1)
    Thruster 4 (-1, 1)
    Thruster 5 (0.5, -0.5)
    Thruster 6 (0.5, 0.5)
    Thruster 7 (-0.5, -0.5)
    Thruster 8 (-0.5, 0.5)
    """
    ANGLE = 0.3839724354  # the angle between the direction of thrust and a line x=n in radians (numpy uses rad)
    xUnit = np.array([1, 0])  # unit vector in the x direction to help find the perpendicular force in torque
    thrusterOffset = np.array([1, 1])  # temp thruster location at (1, 1) can be used for all thrusters for now
    perpForce = np.sin(ANGLE + np.arccos(np.dot(xUnit, thrusterOffset)/np.linalg.norm(thrusterOffset)))  # returns the force perpendicular need to calculate torque
    rotComp = 0.25 / (perpForce * np.linalg.norm(thrusterOffset))

    def __init__(self):
        self.thrustMap = np.array([0, 0, 0, 0, 0, 0])   # list for values that need to be output to the thrusters
        self.mutationMatrix = np.array([[ThrustMapper.xComp, ThrustMapper.yComp, 0, 0, 0, -ThrustMapper.rotComp]
                              [ThrustMapper.xComp, -ThrustMapper.yComp, 0, 0, 0, ThrustMapper.rotComp]
                              [-ThrustMapper.xComp, ThrustMapper.yComp, 0, 0, 0, ThrustMapper.rotComp]
                              [-ThrustMapper.xComp, -ThrustMapper.yrComp, 0, 0, 0, -ThrustMapper.rotComp]
                              [0, 0, 0.25, 0.5, 0.5, 0]  # the values in the fourth and fifth column of the last four rows could be wrong
                              [0, 0, 0.25, -0.5, 0.5, 0]
                              [0, 0, 0.25, 0.5, -0.5, 0]
                              [0, 0, 0.25, -0.5, -0.5, 0]])

    def generate_thrust_map(self, desired):
        """generate the thrustMap to move to the desired vector

        desired (Vector6)
        """
        # some math to determine the thrustMap

        self.thrustMap = np.cross(desired, self.mutationMatrix)
        return self.thrustMap
