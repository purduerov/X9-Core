import Vectors
import matrices


ALL = 0
T1 = 1
T2 = 2
T3 = 3
T4 = 4
T5 = 5
T6 = 6
T7 = 7
T8 = 8
NONE = 9


class ThrustMapperMatrices:

    def __init__(self, currentMapperMatrix, allmatrix, minus_t1, minus_t2, minus_t3, minus_t4, minus_t5, minus_t6, minus_t7,
                 minus_t8, none):
        self.currentMapperMatrix = currentMapperMatrix
        self.matrices = []
        self.matrices[0] = allmatrix
        self.matrices[1] = minus_t1
        self.matrices[2] = minus_t2
        self.matrices[3] = minus_t3
        self.matrices[4] = minus_t4
        self.matrices[5] = minus_t5
        self.matrices[6] = minus_t6
        self.matrices[7] = minus_t7
        self.matrices[8] = minus_t8
        self.matrices[9] = none


class ThrustMapping:

    def __init__(self):
        """note all values are from the maelstrom and need to be replaced when ROV model is made"""
        t1_0 = Vectors.vect6(272, 732, 0, 0, 0, -131)
        t2_0 = Vectors.vect6(272, -732, 0, 0, 0, 131)
        t3_0 = Vectors.vect6(-272, 765, 0, 0, 0, 131)
        t4_0 = Vectors.vect6(-272, -765, 0, 0, 0, -131)
        t5_0 = Vectors.vect6(-19, 14, 228, 181, 236, 0)
        t6_0 = Vectors.vect6(-19, -14, 228, -181, 236, 0)
        t7_0 = Vectors.vect6(19, 14, 284, 181, -236, 0)
        t8_0 = Vectors.vect6(19, -14, 284, -181, -236, 0)

        allmatrix = Vectors.matrix8_6(t1_0, t2_0, t3_0, t4_0, t5_0, t6_0, t7_0, t8_0)

        t1_1 = Vectors.vect6(0,     0,     0,     0,     0,     0)
        t2_1 = Vectors.vect6(0, -1465,     0,     0,     0,   262)
        t3_1 = Vectors.vect6(-545,    32,     0,     0,     0,   262)
        t4_1 = Vectors.vect6(-545, -1497,     0,     0,     0,     0)
        t5_1 = Vectors.vect6(-19,    14,   228,   181,   236,     0)
        t6_1 = Vectors.vect6(-19,   -14,   228,  -181,   236,     0)
        t7_1 = Vectors.vect6(19,    14,   284,   181,  -236,     0)
        t8_1 = Vectors.vect6(19,   -14,   284,  -181,  -236,     0)

        minus_t1 = Vectors.matrix8_6(t1_1, t2_1, t3_1, t4_1, t5_1, t6_1, t7_1, t8_1)

        t1_2 = Vectors.vect6(0, 0, 0, 0, 0, 0)
        t2_2 = Vectors.vect6(0, -1465, 0, 0, 0, 262)
        t3_2 = Vectors.vect6(-545, 32, 0, 0, 0, 262)
        t4_2 = Vectors.vect6(-545, -1497, 0, 0, 0, 0)
        t5_2 = Vectors.vect6(-19, 14, 228, 181, 236, 0)
        t6_2 = Vectors.vect6(-19, -14, 228, -181, 236, 0)
        t7_2 = Vectors.vect6(19, 14, 284, 181, -236, 0)
        t8_2 = Vectors.vect6(19, -14, 284, -181, -236, 0)

        minus_t2 = Vectors.matrix8_6(t1_2, t2_2, t3_2, t4_2, t5_2, t6_2, t7_2, t8_2)

        t1_3 = Vectors.vect6(0, 0, 0, 0, 0, 0)
        t2_3 = Vectors.vect6(0, -1465, 0, 0, 0, 262)
        t3_3 = Vectors.vect6(-545, 32, 0, 0, 0, 262)
        t4_3 = Vectors.vect6(-545, -1497, 0, 0, 0, 0)
        t5_3 = Vectors.vect6(-19, 14, 228, 181, 236, 0)
        t6_3 = Vectors.vect6(-19, -14, 228, -181, 236, 0)
        t7_3 = Vectors.vect6(19, 14, 284, 181, -236, 0)
        t8_3 = Vectors.vect6(19, -14, 284, -181, -236, 0)

        minus_t3 = Vectors.matrix8_6(t1_3, t2_3, t3_3, t4_3, t5_3, t6_3, t7_3, t8_3)

        t1_4 = Vectors.vect6(0, 0, 0, 0, 0, 0)
        t2_4 = Vectors.vect6(0, -1465, 0, 0, 0, 262)
        t3_4 = Vectors.vect6(-545, 32, 0, 0, 0, 262)
        t4_4 = Vectors.vect6(-545, -1497, 0, 0, 0, 0)
        t5_4 = Vectors.vect6(-19, 14, 228, 181, 236, 0)
        t6_4 = Vectors.vect6(-19, -14, 228, -181, 236, 0)
        t7_4 = Vectors.vect6(19, 14, 284, 181, -236, 0)
        t8_4 = Vectors.vect6(19, -14, 284, -181, -236, 0)

        minus_t4 = Vectors.matrix8_6(t1_4, t2_4, t3_4, t4_4, t5_4, t6_4, t7_4, t8_4)

        t1_5 = Vectors.vect6(0, 0, 0, 0, 0, 0)
        t2_5 = Vectors.vect6(0, -1465, 0, 0, 0, 262)
        t3_5 = Vectors.vect6(-545, 32, 0, 0, 0, 262)
        t4_5 = Vectors.vect6(-545, -1497, 0, 0, 0, 0)
        t5_5 = Vectors.vect6(-19, 14, 228, 181, 236, 0)
        t6_5 = Vectors.vect6(-19, -14, 228, -181, 236, 0)
        t7_5 = Vectors.vect6(19, 14, 284, 181, -236, 0)
        t8_5 = Vectors.vect6(19, -14, 284, -181, -236, 0)

        minus_t5 = Vectors.matrix8_6(t1_5, t2_5, t3_5, t4_5, t5_5, t6_5, t7_5, t8_5)

        t1_6 = Vectors.vect6(0, 0, 0, 0, 0, 0)
        t2_6 = Vectors.vect6(0, -1465, 0, 0, 0, 262)
        t3_6 = Vectors.vect6(-545, 32, 0, 0, 0, 262)
        t4_6 = Vectors.vect6(-545, -1497, 0, 0, 0, 0)
        t5_6 = Vectors.vect6(-19, 14, 228, 181, 236, 0)
        t6_6 = Vectors.vect6(-19, -14, 228, -181, 236, 0)
        t7_6 = Vectors.vect6(19, 14, 284, 181, -236, 0)
        t8_6 = Vectors.vect6(19, -14, 284, -181, -236, 0)

        minus_t6 = Vectors.matrix8_6(t1_6, t2_6, t3_6, t4_6, t5_6, t6_6, t7_6, t8_6)

        t1_7 = Vectors.vect6(0, 0, 0, 0, 0, 0)
        t2_7 = Vectors.vect6(0, -1465, 0, 0, 0, 262)
        t3_7 = Vectors.vect6(-545, 32, 0, 0, 0, 262)
        t4_7 = Vectors.vect6(-545, -1497, 0, 0, 0, 0)
        t5_7 = Vectors.vect6(-19, 14, 228, 181, 236, 0)
        t6_7 = Vectors.vect6(-19, -14, 228, -181, 236, 0)
        t7_7 = Vectors.vect6(19, 14, 284, 181, -236, 0)
        t8_7 = Vectors.vect6(19, -14, 284, -181, -236, 0)

        minus_t7 = Vectors.matrix8_6(t1_7, t2_7, t3_7, t4_7, t5_7, t6_7, t7_7, t8_7)

        t1_8 = Vectors.vect6(0, 0, 0, 0, 0, 0)
        t2_8 = Vectors.vect6(0, -1465, 0, 0, 0, 262)
        t3_8 = Vectors.vect6(-545, 32, 0, 0, 0, 262)
        t4_8 = Vectors.vect6(-545, -1497, 0, 0, 0, 0)
        t5_8 = Vectors.vect6(-19, 14, 228, 181, 236, 0)
        t6_8 = Vectors.vect6(-19, -14, 228, -181, 236, 0)
        t7_8 = Vectors.vect6(19, 14, 284, 181, -236, 0)
        t8_8 = Vectors.vect6(19, -14, 284, -181, -236, 0)

        minus_t8 = Vectors.matrix8_6(t1_8, t2_8, t3_8, t4_8, t5_8, t6_8, t7_8, t8_8)

        t1_9 = Vectors.vect6(0, 0, 0, 0, 0, 0)
        t2_9 = Vectors.vect6(0, -1465, 0, 0, 0, 262)
        t3_9 = Vectors.vect6(-545, 32, 0, 0, 0, 262)
        t4_9 = Vectors.vect6(-545, -1497, 0, 0, 0, 0)
        t5_9 = Vectors.vect6(-19, 14, 228, 181, 236, 0)
        t6_9 = Vectors.vect6(-19, -14, 228, -181, 236, 0)
        t7_9 = Vectors.vect6(19, 14, 284, 181, -236, 0)
        t8_9 = Vectors.vect6(19, -14, 284, -181, -236, 0)

        none = Vectors.matrix8_6(t1_9, t2_9, t3_9, t4_9, t5_9, t6_9, t7_9, t8_9)

        self.mapper_matrices = ThrustMapperMatrices(ALL, allmatrix, minus_t1, minus_t2, minus_t3, minus_t4, minus_t5,
                                                    minus_t6, minus_t7, minus_t8, none)

        self.desired_force_vector = Vectors.vect6(0, 0, 0, 0, 0, 0)

        self.pivotPosition = Vectors.vect3(0, 0, 0)

    def calcZeroForceVector(self):
        self.desired_force_vector = Vectors.vect6(0, 0, 0, 0, 0, 0)
        self.calculateThrustMap()

    def adjustPivotPosition(self, loc):
        self.pivotPosition = loc

    def calculateThrustMap(self):
        cross_result = matrices.cross(self.pivotPosition, self.desired_force_vector.R)
        self.desired_force_vector.L.x += cross_result.x
        self.desired_force_vector.L.y += cross_result.y
        self.desired_force_vector.L.z += cross_result.z
        self.thrust_map = matrices.matMul_86x61(self.mapper_matrices.matrices[self.mapper_matrices.currentMapperMatrix],
                                           self.desired_force_vector)

    def calculateThrustMap(self, target_vector):
        self.desired_force_vector = matrices.div6(target_vector, 1024)

        cross_result = matrices.cross(self.pivotPosition, self.desired_force_vector.R)
        self.desired_force_vector.L.x += cross_result.x
        self.desired_force_vector.L.y += cross_result.y
        self.desired_force_vector.L.z += cross_result.z
        self.thrust_map = matrices.matMul_86x61(self.mapper_matrices.matrices[self.mapper_matrices.currentMapperMatrix],
                                           self.desired_force_vector)

    def changMapperMatrix(self, enabled_thrusters):
        if enabled_thrusters == 255:
            self.mapper_matrices.currentMapperMatrix = ALL
        elif enabled_thrusters == 254:
            self.mapper_matrices.currentMapperMatrix = T8
        elif enabled_thrusters == 253:
            self.mapper_matrices.currentMapperMatrix = T7
        elif enabled_thrusters == 251:
            self.mapper_matrices.currentMapperMatrix = T6
        elif enabled_thrusters == 247:
            self.mapper_matrices.currentMapperMatrix = T5
        elif enabled_thrusters == 239:
            self.mapper_matrices.currentMapperMatrix = T4
        elif enabled_thrusters == 223:
            self.mapper_matrices.currentMapperMatrix = T3
        elif enabled_thrusters == 191:
            self.mapper_matrices.currentMapperMatrix = T2
        elif enabled_thrusters == 127:
            self.mapper_matrices.currentMapperMatrix = T1
        elif enabled_thrusters == 0:
            self.mapper_matrices.currentMapperMatrix = NONE
        else:
            self.mapper_matrices.currentMapperMatrix = NONE

    def getCurrentForceVector(self):
        return self.desired_force_vector

    def getThrustMap(self):
        return self.thrust_map

    def getPivotPosition(self):
        return self.pivotPosition
