import numpy as np
import thrustMapperMatrix as mm


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
        self.maker = mm.MutatorMatrix()
        """self.maker = mutatormatrix.MutatorMatrix(-4.7524,0,11.2148,4.7524,0,11.2148,
                                             -4.7524,0,-7.631,4.7524,0,-7.631,
                                             -5.5709,5.6384,6.0419,
                                             5.5709,5.6384,6.0419,
                                             -5.5709,5.6384,-2.485,
                                             5.5709,5.6384,-2.485)"""
        # self.mutationMatrix = self.maker.generate_matrix()
        self.mutationMatrix = self.maker.generateMatrix()

    def generate_thrust_map(self, enabledThrusters, desired):
        """generate the thrustMap to move to the desired vector

        desired (Vector6)
        """
        if not np.array_equal(enabledThrusters, self.maker.thrusterStatus):
            self.mutationMatrix = self.maker.setThrusterStatus(enabledThrusters)
        # some math to determine the thrustMap
        self.thrustMap = self.mutationMatrix.dot(desired)
        if self.thrustMap.max() > 1:
            self.thrustMap[:, :] *= (1 / self.thrustMap.max())
        if self.thrustMap.min() < -1:
            self.thrustMap[:, :] *= (-1 / self.thrustMap.min())
        return self.thrustMap

def printMatrix(mutatorMatrix):
    for i in range(0, 8):
        print "[%f,\t%f,\t%f,\t%f,\t%f,\t%f]," % (mutatorMatrix[i,0], mutatorMatrix[i,1], mutatorMatrix[i,2], mutatorMatrix[i,3], mutatorMatrix[i,4], mutatorMatrix[i,5])
    print "\n\n"

if __name__ == "__main__":
    mapper = ThrustMapper()
    mutatorMatrix = mapper.mutationMatrix
    print "********** Mutation Matrix **********"
    printMatrix(mapper.mutationMatrix)
    thrusters = np.array([1, 1, 1, 1, 1, 1, 1, 1])

    desired = np.array([[1], [0], [0], [0], [0], [0]])
    print "********** Thruster Output 1X **********"
    print mapper.generate_thrust_map(thrusters, desired)
    print "\n\n"

    desired = np.array([[0], [1], [0], [0], [0], [0]])
    print "********** Thruster Output 1Y **********"
    print mapper.generate_thrust_map(thrusters, desired)
    print "\n\n"

    desired = np.array([[0], [0], [1], [0], [0], [0]])
    print "********** Thruster Output 1Z **********"
    print mapper.generate_thrust_map(thrusters, desired)
    print "\n\n"

    desired = np.array([[0], [0], [0], [1], [0], [0]])
    print "********** Thruster Output 1 Rotation about Z **********"
    print mapper.generate_thrust_map(thrusters, desired)
    print "\n\n"

    desired = np.array([[0], [0], [0], [0], [1], [0]])
    print "********** Thruster Output 1 Rotation about X **********"
    print mapper.generate_thrust_map(thrusters, desired)
    print "\n\n"
    
    desired = np.array([[1], [1], [0], [0], [0], [1]])
    print "********** Thruster Output MAX X Y ROT Z **********"
    print mapper.generate_thrust_map(thrusters, desired)
    print "\n\n"
