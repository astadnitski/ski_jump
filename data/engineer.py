import numpy as np
from scipy.optimize import curve_fit

# defining function
def y(x,a,b):
        return a*x+b*x**2

def vel(x,a,b):
        return a+2*b*x
        
def initialCond(a,b): 
        velocity=vel(0,a,b)
        angle=np.arcsin(velocity/a)
        return velocity, angle
#Import initial cond
np.loadtxt("A-test.txt")
data=np.loadtxt("A-test.txt")
xdata = table[:,0]
ydata = table[:,1]
# fit
curve_fit(y, xdata, ydata)

        

initialCond(a,b)

