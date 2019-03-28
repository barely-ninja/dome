from numpy import array, dot, round
from math import pi, sin, cos

vert = array([
    [0.19612, 0, -0.98058],
    [0.2357, 0.2357, -0.94281],
    [0.44722, 0, -0.89442],
    [0.53452, 0.26726, -0.80179],
    [0.57735, 0.57735, -0.57735],
    [0.70711, 0, -0.70711],
    [0.80179, 0.26726, -0.53452],
    [0.80179, 0.53452, -0.26726],
    [0.89442, 0, -0.44722],
    [0.94281, 0.2357, -0.2357],
    [0.98058, 0, -0.19612],
    [0.89443,0.44722,0],
    [0.89443,0,0.44722]
])

ang = 45.*pi/180.
c = cos(ang)
s = sin(ang)
rot = array([
    [c,s,0],
    [-s,c,0],
    [0,0,1]
])
vr = dot(vert, rot)

result = round(vr*4.24+array([0,0,3]),2)
#v3
#result = round(vert*2.6+array([0,0,1.5]),2)[[4,8,-1],:]
print(result)