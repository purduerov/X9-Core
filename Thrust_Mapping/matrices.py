import Vectors


def dot6(a, b):
    """a and b should be vect6 objects"""
    return dot(a.L, b.L) + dot(a.R, b.R)


def dot(a, b):
    """a and b should be vect3 objects"""
    return a.x * b.x + a.y * b.y + a.z * b.z


def dot2(a, b):
    """a and b should be vect2 objects"""
    return a.a * b.a + a.b * b.b


def cross(a, b):
    """returns the cross product of a and b"""
    x = a.y * b.z - a.z * b.y
    y = a.z * b.x - a.x * b.z
    z = a.x * b.y - a.y * b.x
    return Vectors.vect3(x, y, z)


def add(a, b):
    """adds the sum of vectors a and b"""
    x = a.x + b.x
    y = a.y + b.y
    z = a.z + b.z
    return Vectors.vect3(x, y, z)


def add6(a, b):
    """adds the sum of the vect6s a and b"""
    L = add(a.L, b.L)
    R = add(a.R, b.R)
    return Vectors.vect6(L.x, L.y, L.z, R.x, R.y, R.z)


def sub(a, b):
    """subtract vector b from vector a"""
    x = a.x - b.x
    y = a.y - b.y
    z = a.z - b.z
    return Vectors.vect3(x, y, z)


def sub6(a, b):
    """subtract b from a"""
    L = sub(a.L, b.L)
    R = sub(a.R, b.R)
    return Vectors.vect6(L.x, L.y, L.z, R.x, R.y, R.z)


def mul(a, factor):
    """multiply vector a by factor"""
    x = a.x * factor
    y = a.y * factor
    z = a.z * factor
    return Vectors.vect3(x, y, z)


def mul6(a, factor):
    """multiply vact6 a by factor"""
    L = mul(a.L, factor)
    R = mul(a.R, factor)
    return Vectors.vect6(L.x, L.y, L.z, R.x, R.y, R.z)


def div(a, factor):
    """multiply vector a by factor"""
    x = a.x / factor
    y = a.y / factor
    z = a.z / factor
    return Vectors.vect3(x, y, z)


def div6(a, factor):
    """multiply vact6 a by factor"""
    L = div(a.L, factor)
    R = div(a.R, factor)
    return Vectors.vect6(L.x, L.y, L.z, R.x, R.y, R.z)


def max3(vect):
    """max value in vect3"""
    return max(vect.a.x, vect.a.y, vect.a.z)


def max6(vect):
    """return the max value in vect6"""
    return max(vect.L.x, vect.L.y, vect.L.z, vect.R.x, vect.R.y, vect.R.z)


def max8(vect):
    """return the max value in vect8"""
    return max(vect.a, vect.b, vect.c, vect.d, vect.e, vect.f, vect.g, vect.h)


def matMul_86x61(mat, v):
    a = dot6(mat.t1, v)
    b = dot6(mat.t2, v)
    c = dot6(mat.t3, v)
    d = dot6(mat.t4, v)
    e = dot6(mat.t5, v)
    f = dot6(mat.t6, v)
    g = dot6(mat.t7, v)
    h = dot6(mat.t8, v)
    return Vectors.vect8(a, b, c, d, e, f, g, h)


def matMul_33x31(m, v):
    x = dot(m.a, v)
    y = dot(m.b, v)
    z = dot(m.c, v)
    return Vectors.vect3(x, y, z)


def matMul_22x22(a, b):
    """both inputs are matrix2_2"""
    a1 = dot2(a.one, Vectors.vect2(b.one.a, b.two.a))
    b1 = dot2(a.one, Vectors.vect2(b.one.b, b.two.b))
    one = Vectors.vect2(a1, b1)
    a2 = dot2(a.two, Vectors.vect2(b.one.a, b.two.a))
    b2 = dot2(a.two, Vectors.vect2(b.one.b, b.two.b))
    two = Vectors.vect2(a2, b2)
    return Vectors.matrix2_2(one, two)


def invert2_2(m):
    det = m.one.a * m.one.b - m.one.b * m.two.a
    a1 = m.two.b * 1024 / det
    b1 = -m.one.b * 1024 / det
    a2 = -m.two.a * 1024 / det
    b2 = m.one.a * 1024 / det
    one = Vectors.vect2(a1, b1)
    two = Vectors.vect2(a2, b2)
    return Vectors.matrix2_2(one, two)