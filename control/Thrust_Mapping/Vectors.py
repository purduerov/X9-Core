class vect6(object):
    """
    A 6 Dimensional Vector

    L (vect3):
    R (vect3):
    """

    def __init__(self, x, y, z, rho, theta, phi):
        self.L = vect3(x,y,z)
        self.R = vect3(rho, theta, phi)


class vect3(object):
    """
    A 3 Dimensional Vector

    x (double):
    y (double):
    z (double):
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class vect2(object):
    """
    A 2 Dimensional Vector

    a (double):
    b (double):
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b


class vect8(object):
    """A 8 Dimensional Vector

    a (double):
    b (double):
    c (double):
    d (double):
    e (double):
    f (double):
    g (double):
    h (double):
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


class matrix8_6(object):
    """
    An 8x6 Matrix made from 8 vect6 objects

    t1 (vect6):
    t2 (vect6):
    t3 (vect6):
    t4 (vect6):
    t5 (vect6):
    t6 (vect6):
    t7 (vect6):
    t8 (vect6):
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


class matrix8_3(object):
    """
    An 8x3 Matrix made from 8 vect3 objects

    t1 (vect3):
    t2 (vect3):
    t3 (vect3):
    t4 (vect3):
    t5 (vect3):
    t6 (vect3):
    t7 (vect3):
    t8 (vect3):
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


class matrix3_3(object):
    """
    A 3x3 Matrix made from 3 vect3 objects

    a (vect3):
    b (vect3):
    c (vect3):
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class matrix2_2(object):
    """
    A 2x2 Matrix made from 2 vect2 objects

    one (vect2):
    two (vect2):
    """
    def __init__(self, one, two):
        self.one = one
        self.two = two