from scipy.optimize import leastsq
from numpy import array, concatenate, newaxis
from numpy.linalg import norm

def make_d(p1,d):
    def f(x):
        nx = norm(x)
        np = norm(p1-x)
        return array([(nx-1)**2,(np-d)**2])
    return f 

def make_d(p,d):
    def f(x):
        nx = concatenate([norm(x)[newaxis], norm(p-x, axis=1)])
        dx = concatenate([array([1.]), d])
        return (nx-dx)*(nx-dx) 
    return f

#fs = lambda x: f(array([x[0], 0, x[1]]))

p = array([[0.57735,0.57735,-0.57735],[0.80179, 0.26726, -0.53452],[0.94281,0.2357,-0.2357]])
d = array([0.38518, 0.37796, 0.33193])
f = make_d(p, d)
x0 = array([0.7, 0.6, -0.36])
x, succ = leastsq(f, x0)
print(x)