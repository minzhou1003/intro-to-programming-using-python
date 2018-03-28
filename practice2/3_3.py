# copyright minzhou@bu.edu

import math

x1 = 51.5138505182
y1 = -0.15690922737098845

x2 = 28.5383355
y2 = -81.37923649999999 

x3 = 32.0835407
y3 = -81.09983419999998

x4 = 35.2270869
y4 = -80.84312669999997

def dist(x1, x2, y1, y2):
    d = 6371.01 * math.acos((
        math.sin(math.radians(x1)) * 
        math.sin(math.radians(x2))) +
        math.cos(math.radians(x1)) *
        math.cos(math.radians(x2)) *
        math.cos(math.radians(y1) - math.radians(y2)))
    return d

def triangle(s1, s2, s3):
    s = (s1 + s2 + s3) / 2.0
    return math.pow(s * (s - s1) * (s - s2) * (s - s3), 0.5)

s1 = dist(x1, x2, y1, y2)
s2 = dist(x1, x3, y1, y3)
s3 = dist(x1, x4, y1, y4)
s4 = dist(x2, x3, y2, y3)
s5 = dist(x2, x4, y2, y4)
s6 = dist(x3, x4, y3, y4)

def istriangle(s1, s2, s3):
    return ((s1 + s2 > s3) and (s1 + s3 > s2) and (s3 + s2 > s1))

if (istriangle(s1, s2, s3) and istriangle(s4, s5, s6)):
    res = triangle(s1, s2, s3) + triangle(s4, s5, s6)
print('The estimated area enclosed by these four cities is ' + str(res))