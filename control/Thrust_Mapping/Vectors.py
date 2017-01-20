class Vector6(object):
    """
    A 6 Dimensional Vector

    L (Vector3)
    R (Vector3)
    """

    def __init__(self, x, y, z, rho, theta, phi):
        self.L = Vector3(x, y, z)
        self.R = Vector3(rho, theta, phi)


class Vector3(object):
    """
    A 3 Dimensional Vector

    x (double)
    y (double)
    z (double)
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Vector2(object):
    """
    A 2 Dimensional Vector

    a (double)
    b (double)
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Vector8(object):
    """A 8 Dimensional Vector

    a (double)
    b (double)
    c (double)
    d (double)
    e (double)
    f (double)
    g (double)
    h (double)
    """
    def __init__(self, a, b, c, d, e, f, g, h):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h


class Matrix8x6(object):
    """
    An 8x6 Matrix made from 8 Vector6 objects

    t1 (Vector6)
    t2 (Vector6)
    t3 (Vector6)
    t4 (Vector6)
    t5 (Vector6)
    t6 (Vector6)
    t7 (Vector6)
    t8 (Vector6)
    """
    def __init__(self, t1, t2, t3, t4, t5, t6, t7, t8):
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.t7 = t7
        self.t8 = t8


class Matrix8x3(object):
    """
    An 8x3 Matrix made from 8 Vector3 objects

    t1 (Vector3)
    t2 (Vector3)
    t3 (Vector3)
    t4 (Vector3)
    t5 (Vector3)
    t6 (Vector3)
    t7 (Vector3)
    t8 (Vector3)
    """
    def __init__(self, t1, t2, t3, t4, t5, t6, t7, t8):
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.t7 = t7
        self.t8 = t8


class Matrix3x3(object):
    """
    A 3x3 Matrix made from 3 Vector3 objects

    a (Vector3)
    b (Vector3)
    c (Vector3)
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class Matrix2x2(object):
    """
    A 2x2 Matrix made from 2 Vector2 objects

    one (Vector2)
    two (Vector2)
    """
    def __init__(self, one, two):
        self.one = one
        self.two = two
