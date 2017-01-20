import Vectors


class Matrices(object):
    """Container Class for different Vector and Matrix operations"""

    @staticmethod
    def dot6(a, b):
        """dot Vector6 a with Vector6 b and return the resulting scalar

        a (Vector6)
        b (Vector6)
        """
        return Matrices.dot(a.L, b.L) + Matrices.dot(a.R, b.R)

    @staticmethod
    def dot(a, b):
        """dot Vector3 a with Vector3 b and return the resulting scalar
        a (Vector3)
        b (Vector3)
        """
        return a.x * b.x + a.y * b.y + a.z * b.z

    @staticmethod
    def dot2(a, b):
        """dot Vector2 a and Vector2 b and return the resulting scalar

        a (Vector2)
        b (Vector2)
        """
        return a.a * b.a + a.b * b.b

    @staticmethod
    def cross(a, b):
        """cross Vector3 a with Vector3 b and return the resulting Vector3

        a (Vector3)
        b (Vector3)
        """
        x = a.y * b.z - a.z * b.y
        y = a.z * b.x - a.x * b.z
        z = a.x * b.y - a.y * b.x
        return Vectors.Vector3(x, y, z)

    @staticmethod
    def add(a, b):
        """adds Vector3 a and Vector3 b and returns the resulting Vector3

        a (Vector3)
        b (Vector3)
        """
        x = a.x + b.x
        y = a.y + b.y
        z = a.z + b.z
        return Vectors.Vector3(x, y, z)

    @staticmethod
    def add6(a, b):
        """adds Vector6 a and Vector6 b and returns the resulting Vector6

        a (Vector6)
        b (Vector6)
        """
        left = Matrices.add(a.L, b.L)
        right = Matrices.add(a.R, b.R)
        return Vectors.Vector6(left.x, left.y, left.z, right.x, right.y, right.z)

    @staticmethod
    def sub(a, b):
        """subtract Vector3 b from Vector3 a and returns the resulting Vector3

        a (Vector3)
        b (Vector3)
        """
        x = a.x - b.x
        y = a.y - b.y
        z = a.z - b.z
        return Vectors.Vector3(x, y, z)

    @staticmethod
    def sub6(a, b):
        """subtract Vector6 b from Vector6 a and returns the resulting Vector6

        a (Vector6)
        b (Vector6)
        """
        left = Matrices.sub(a.L, b.L)
        right = Matrices.sub(a.R, b.R)
        return Vectors.Vector6(left.x, left.y, left.z, right.x, right.y, right.z)

    @staticmethod
    def mul(a, factor):
        """multiply Vector3 a by factor and return the resulting Vector3

        a (Vector3)
        factor (double)
        """
        x = a.x * factor
        y = a.y * factor
        z = a.z * factor
        return Vectors.Vector3(x, y, z)

    @staticmethod
    def mul6(a, factor):
        """multiply Vector6 a by factor and return the resulting Vector6

        a (Vector6)
        factor (double)
        """
        left = Matrices.mul(a.L, factor)
        right = Matrices.mul(a.R, factor)
        return Vectors.Vector6(left.x, left.y, left.z, right.x, right.y, right.z)

    @staticmethod
    def div(a, factor):
        """divide Vector3 a by factor and return the resulting Vector3

        a (Vector3)
        factor (double)
        """
        x = a.x / factor
        y = a.y / factor
        z = a.z / factor
        return Vectors.Vector3(x, y, z)

    @staticmethod
    def div6(a, factor):
        """divide Vector6 a by factor and return the resulting Vector6

        a (Vector6)
        factor (double)
        """
        left = Matrices.div(a.L, factor)
        right = Matrices.div(a.R, factor)
        return Vectors.Vector6(left.x, left.y, left.z, right.x, right.y, right.z)

    @staticmethod
    def max3(vect):
        """max value in Vector3 vect

        vect (Vector3)
        """
        return max(vect.a.x, vect.a.y, vect.a.z)

    @staticmethod
    def max6(vect):
        """return the max value in Vector6 vect

        vect (Vector6)
        """
        return max(vect.L.x, vect.L.y, vect.L.z, vect.R.x, vect.R.y, vect.R.z)

    @staticmethod
    def max8(vect):
        """return the max value in Vector8 vect

        vect (Vector8)
        """
        return max(vect.a, vect.b, vect.c, vect.d, vect.e, vect.f, vect.g, vect.h)

    @staticmethod
    def matmul_86x61(mat, v):
        """multiply Matrix8x6 mat by Vector6 v and return the resulting Vector8

        mat (Matrix8x6)
        v (Vector6)
        """
        a = Matrices.dot6(mat.t1, v)
        b = Matrices.dot6(mat.t2, v)
        c = Matrices.dot6(mat.t3, v)
        d = Matrices.dot6(mat.t4, v)
        e = Matrices.dot6(mat.t5, v)
        f = Matrices.dot6(mat.t6, v)
        g = Matrices.dot6(mat.t7, v)
        h = Matrices.dot6(mat.t8, v)
        return Vectors.Vector8(a, b, c, d, e, f, g, h)

    @staticmethod
    def matmul_33x31(m, v):
        """multiply Matrix3x3 m by Vector3 v and return the resulting Vector3

        m (Matrix3x3)
        v (Vector3)
        """
        x = Matrices.dot(m.a, v)
        y = Matrices.dot(m.b, v)
        z = Matrices.dot(m.c, v)
        return Vectors.Vector3(x, y, z)

    @staticmethod
    def matmul_22x22(a, b):
        """multiply Matrix2x2 a by Matrix2x2 and return the resulting Matrix2x2

        a (Matrix2x2)
        b (Matrix2x2)
        """
        a1 = Matrices.dot2(a.one, Vectors.Vector2(b.one.a, b.two.a))
        b1 = Matrices.dot2(a.one, Vectors.Vector2(b.one.b, b.two.b))
        one = Vectors.Vector2(a1, b1)
        a2 = Matrices.dot2(a.two, Vectors.Vector2(b.one.a, b.two.a))
        b2 = Matrices.dot2(a.two, Vectors.Vector2(b.one.b, b.two.b))
        two = Vectors.Vector2(a2, b2)
        return Vectors.Matrix2x2(one, two)

    @staticmethod
    def invert2_2(m):
        """invert Matrix2x2 m and return the result

        m (Matrix2x2)
        """
        det = m.one.a * m.one.b - m.one.b * m.two.a
        a1 = m.two.b * 1024 / det
        b1 = -m.one.b * 1024 / det
        a2 = -m.two.a * 1024 / det
        b2 = m.one.a * 1024 / det
        one = Vectors.Vector2(a1, b1)
        two = Vectors.Vector2(a2, b2)
        return Vectors.Matrix2x2(one, two)
