"""
Numerical methods for solving the equation
"""
# ATTENTION: f is the function attach to the equation, dif is the differential of function f, a is the lower gauss of solution to the equation, b is the upper gauss to the equation.
# Use package numpy
import numpy as np
# Tolerance
tolerance=[0.000000001]
# Bisection method
def bisection(f,a,b):
    i=0
    while(abs(b-a)>tolerance[0]):
        i=i+1
        if(f(0.5*(a+b))==0):
            a=0.5*(a+b)
        else:
            if(f(a)*f(0.5*(a+b))<0):
                b=0.5*(a+b)
            if(f(0.5*(a+b))*f(b)<0):
                a=0.5*(a+b)
    return(a,i)
# Newton method
def newton(f,dif,a,b):
    i=0
    while(abs()>tolerance):
        i=i+1
        a=a-f(a)/dif(a)
    return(a,i)
# String cut method
def stringcut(f,a,b):
    i=0
    c=b-f(b)*((b-a)/(f(b)-f(a)))
    while(abs(c-a)>tolerance[0]):
        i=i+1
        c=b-f(b)*((b-a)/f(b)-f(a))
        a=b
        b=c
    return(c,i)
