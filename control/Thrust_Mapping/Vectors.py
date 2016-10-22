class vect6:

    def __init__(self, x, y, z, rho, theta, phi):
        self.L = vect3(x,y,z)
        self.R = vect3(rho, theta, phi)


class vect3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class vect2:

    def __init__(self, a, b):
        self.a = a
        self.b = b


class vect8:

    def __init__(self, a, b, c, d, e, f, g, h):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h


class matrix8_6:

    def __init__(self, t1, t2, t3, t4, t5, t6, t7, t8):
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.t7 = t7
        self.t8 = t8


class matrix8_3:

    def __init__(self, t1, t2, t3, t4, t5, t6, t7, t8):
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.t7 = t7
        self.t8 = t8


class matrix3_3:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class matrix2_2:

    def __init__(self, one, two):
        self.one = one
        self.two = two
