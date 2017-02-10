import numpy as np


class MutatorMatrix(object):

    def __init__(self):

        """these are the locations of the thrusters given in X, Y, Z
        coordinates are X is foward/backwards (foward is positive)
        Y is right/left (right is positive)
        Z is up/down (up is positive)
        each row is a thruster given in XYZ"""
        self.X_9 = np.matrix([[5.575, -6.59, 0],
                                [5.575, 6.59, 0],
                                [-5.575, -6.34, 0],
                                [-5.575, 6.34, 0],
                                [3.925, -7.19, 1.95],
                                [3.925, 7.19, 1.95],
                                [-2.575, -7.19, 1.95],
                                [-2.575, 7.19, 1.95]])

        self.TORNADO = np.matrix([[11.2148, -4.7524, 0],
                                [11.2148, 4.7524, 0],
                                [-7.631, -4.7524, 0],
                                [-7.631, 4.7524, 0],
                                [6.0419, -5.5709, 5.6384],
                                [6.0419, 5.5709, 5.6384],
                                [-2.485, -5.5709, 5.6384],
                                [-2.485, 5.5709, 5.6384]])

        self.TORNADO_COM = np.matrix([[1.31, 0.0, 0.31],
                                    [1.31, 0.0, 0.31],
                                    [1.31, 0.0, 0.31],
                                    [1.31, 0.0, 0.31],
                                    [1.31, 0.0, 0.31],
                                    [1.31, 0.0, 0.31],
                                    [1.31, 0.0, 0.31],
                                    [1.31, 0.0, 0.31]])

        # adjust thruster locations for center of mass
        self.TORNADO = self.TORNADO - self.TORNADO_COM

        self.loc = np.transpose(self.X_9)
        self.loc *= .0254
        # get second coordinate to make point on the unit sphere
        z = np.sqrt(1-.342*.342)
        """these are the rotation components of each thruster given by putting origin on the thruster
        the direction is given by drawing a line from the origin to the point on the unit sphere (given in X, Y, Z)
        XYZ are the same as for locations"""
        self.rot = np.transpose(np.matrix([[z, 0.342, 0],
                                           [z, -0.342, 0],
                                           [-z, 0.342, 0],
                                           [-z, -0.342, 0],
                                           [0, 0, 1],
                                           [0, 0, 1],
                                           [0, 0, 1],
                                           [0, 0, 1]]))
        # used for some manipulation later
        self.m = None
        self.thrusterStatus = [1, 1, 1, 1, 1, 1, 1, 1]
        self.mutationMatrix = None

    def generateMatrix(self):
        self.m = self.rot
        # find the cross of the rotation and location matrix
        # there are alot of transposes because it wouldn't run for me otherwise
        temp = np.transpose(np.cross(np.transpose(self.rot), np.transpose(self.loc), 1))
        # concatenates the two matrices together
        self.m = np.concatenate((self.m, temp))
        # turn off thrusters for whatever reason
        self.turnOffThruster()
        # determine the pseudo inverse of the matrix which gives the final mutation matrix
        matrix = np.linalg.pinv(self.m)
        # scale slightly
        matrix[:, 3:6] = matrix[:, 3:6] / 10
        self.mutationMatrix = matrix
        return self.mutationMatrix

    def turnOffThruster(self):
        """
        turns of the appropriate thrusters when the matrix is being generated if value is 1 it is off
        :return:
        """
        for i in range(0, 8):
            if self.thrusterStatus[i] == 0:
                self.m[:, i] = 0
    
    def setThrusterStatus(self, enabledThrusters):
        # checks to see if the thrusters have changed state and if a new matrix needs to be generated
        self.thrusterStatus = enabledThrusters
        return self.generateMatrix()

if __name__ == "__main__":
    matrix = MutatorMatrix()
    mutatorMatrix = matrix.generateMatrix()
    for i in range(0, 8):
        print "[%f,\t%f,\t%f,\t%f,\t%f,\t%f]," % (mutatorMatrix[i, 0], mutatorMatrix[i, 1], mutatorMatrix[i, 2], mutatorMatrix[i, 3], mutatorMatrix[i, 4], mutatorMatrix[i, 5])
    # print matrix.generateMatrix()

