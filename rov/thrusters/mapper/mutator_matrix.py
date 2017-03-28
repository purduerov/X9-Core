import numpy as np


class Mapper(object):

    def __init__(self):
        """ These are the locations of the thrusters given in X, Y, Z
        coordinates are X is foward/backwards (foward is positive) Y is
        right/left (right is positive) Z is up/down (up is positive) each row
        is a thruster given in XYZ. Positions are in inches!
        """

        # a basic thruster configuration
        self.BASIC = np.matrix([
            [+6, -6,  0],
            [+6, +6,  0],
            [-6, -6,  0],
            [-6, +6,  0],
            [+4, -6, +2],
            [+4, +6, +2],
            [-4, -6, +2],
            [-4, +6, +2],
        ])

        # ROV X9 configuration
        self.X9 = np.matrix([
            [5.575, -6.59, 0],
            [5.575, 6.59, 0],
            [-5.575, -6.34, 0],
            [-5.575, 6.34, 0],
            [3.925, -7.19, 1.95],
            [3.925, 7.19, 1.95],
            [-2.575, -7.19, 1.95],
            [-2.575, 7.19, 1.95]
        ])

        # ROV Maelstrom configuration
        self.MAELSTROM = np.matrix([
            [11.2148, -4.7524, 0],
            [11.2148, 4.7524, 0],
            [-7.631, -4.7524, 0],
            [-7.631, 4.7524, 0],
            [6.0419, -5.5709, 5.6384],
            [6.0419, 5.5709, 5.6384],
            [-2.485, -5.5709, 5.6384],
            [-2.485, 5.5709, 5.6384]
        ])

        # ROV Maelstrom Center of Mass offset
        self.MAELSTROM_COM = np.matrix([
            [1.31, 0.0, 0.31],
            [1.31, 0.0, 0.31],
            [1.31, 0.0, 0.31],
            [1.31, 0.0, 0.31],
            [1.31, 0.0, 0.31],
            [1.31, 0.0, 0.31],
            [1.31, 0.0, 0.31],
            [1.31, 0.0, 0.31]
        ])

        # adjust thruster locations for center of mass
        self.MAELSTROM = self.MAELSTROM - self.MAELSTROM_COM

        # select X9 to be used in mapper calculation
        self.THRUSTER_MATRIX = self.X9

        # needs to be transposed
        self.loc = np.transpose(self.THRUSTER_MATRIX)

        # convert from inches to meters
        self.loc *= .0254

        # get second coordinate to make point on the unit sphere
        z = np.sqrt(1-.342*.342)
        """ These are the rotation components of each thruster given by putting
        origin on the thruster the direction is given by drawing a line from
        the origin to the point on the unit sphere (given in X, Y, Z) XYZ are
        the same as for locations
        """
        self.rot = np.transpose(np.matrix([
            [z, 0.342, 0],
            [z, -0.342, 0],
            [-z, 0.342, 0],
            [-z, -0.342, 0],
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1]
        ]))

        # empty set
        self.disabled_thrusters = set()

        self.mutation_matrix = None
        self.generateMatrix()

    def calculate(self, desired_thrust, disabled_thrusters=[]):
        """ Generate the thrustMap to move to the desired vector

        desired_thruster: List [X, Y, Z, Roll, Pitch, Yaw]
        disabled_thrusters: List of disabled thrusters (Values are in range [1, 8])
        """

        # Check the set of disabled_thrusters against the previously set set
        # If they do not match, then we need to regerenate the map. Otherwise
        # calculate the desired thrust
        new_disabled_thrusters = set(disabled_thrusters)
        if new_disabled_thrusters != self.disabled_thrusters:
            self.disabled_thrusters = new_disabled_thrusters
            self.generateMatrix()

        # The thrust mapping is the mutation matrix (dot) desired_thrust
        thrust_map = self.mutationMatrix.dot(desired_thrust)

        # normalize map between [-1, 1]
        max_val = max(abs(thrust_map.max()), abs(thrust_map.min()))
        if max_val > 1.0:
            thrust_map /= float(max_val)

        return thrust_map

    def generateMatrix(self):
        m = self.rot

        # find the cross of the rotation and location matrix
        # there are a lot of transposes because it wouldn't run otherwise
        temp = np.transpose(
            np.cross(np.transpose(self.rot), np.transpose(self.loc), 1)
        )

        # concatenates the two matrices together
        m = np.concatenate((m, temp))

        # clears out the column of the matrix if a thruster is disabled
        # disabled thrusters are 1-indexed
        for t in self.disabled_thrusters:
            if 1 <= t <= 8:
                m[:, t-1] = 0.0

        # determine the pseudo inverse of the matrix which gives the final
        # mutation matrix
        matrix = np.linalg.pinv(m)

        # scale slightly
        matrix[:, 3:6] = matrix[:, 3:6] / 10

        self.mutationMatrix = matrix

if __name__ == "__main__":
    matrix = Mapper()
    mutatorMatrix = matrix.generateMatrix()
    for m in mutatorMatrix:
        print("[%+.5f, %+.5f, %+.5f, %+.5f, %+.5f, %+.5f]" % tuple(m.tolist()[0]))
