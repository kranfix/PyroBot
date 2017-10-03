from sympy import *
t = symbols('t')

def Rot(axis, angle):
    if axis == 'x':
        return Matrix([ [1,0,0], [0, cos(angle), -sin(angle)], [0, sin(angle), cos(angle)] ])
    elif axis == 'y':
        return Matrix([ [cos(angle), 0, sin(angle)], [0,1,0], [-sin(angle), 0, cos(angle)] ])
    elif axis == 'z':
        return Matrix([ [cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0,0,1]])
    else:
        cs = cos(angle)
        sn = sin(angle)
        v = 1 - cos(angle)
        kx = axis[0]
        ky = axis[1]
        kz = axis[2]
        return Matrix([ [kx**2 * v + cs, kx*ky*v-kz*sn, kx*kz*v+ky*sn],
                        [kx*ky*v+kz*sn, ky**2*v+cs, ky*kz*v-kx*sn],
                        [kx*kz*v-ky*sn, ky*kz*v+kx*sn, kz**2*v+cs]])

def Pos(axis, distance):
    DV = zeros(3,1)
    if axis == 'x':
        DV = Matrix([ [distance], [0], [0] ])
    elif axis == 'y':
        DV = Matrix([ [0], [distance], [0] ])
    elif axis == 'z':
        DV = Matrix([ [0], [0], [distance] ])
    elif len(distance) == 3:
        DV = distance
    elif len(distance) == 4:
        DV = distance[0:3,0]
    else:
        DV = distance * axis
    return DV

def PosH(axis, distance):
    PosH = ones(4,1)
    PosH[0,0] = Pos(axis, distance)
    return PosH

def Hom(axis, angle, distance):
    HM = eye(4)
    HM[0,0] = Rot(axis,angle)
    HM[0,3] = Pos(axis, distance)
    return HM

def HomR(axis,angle):
    HM = Hom(axis,angle,0)
    return HM

def HomT(axis,distance):
    HM = Hom(axis, 0, distance)
    return HM
            
def Skew(vector):
    if(vector == 'x'):
        return Matrix([ [0,0,0], [0,0,-1], [0,1,0] ])
    elif(vector == 'y'):
        return Matrix([ [0,0,1], [0,0,0], [-1,0,0] ])
    elif(vector == 'z'):
        return Matrix([ [0,-1,0], [1,0,0], [0,0,0] ])
    else:
        ax = vector[0]
        ay = vector[1]
        az = vector[2]
        return Matrix([ [0, -az, ay], [az, 0, ax], [-ay, ax, 0] ])

