"""
Numerical Methods for Integration
"""
# ATTENTION: f is the integrand, a is the lower limit, b is the upper limit.
# Use package numpy
import numpy as np
# The number of integration steps
N=[1000] # You can choose the number of integration steps by change the number inside the []
# Rectangle Integration
def rectangle(f,a,b):
    I=0;x=a;h=(b-a)/(int)(N[0])
    for i in range((int)(N[0])):
        I=I+f(x)*h
        x=x+h
    return(I)
# Trapezoid Integration
def tapezoid(f,a,b):
    I=0;x=a;h=(b-a)/((int)(N[0]))
    for i in range((int)(N[0])):
        I=I+(0.5)*(f(x)+f(x+h))*h
        x=x+h
    return(I)
# Simpson Integration
def simpson(f,a,b):
    s1=0.0;s2=0.0
    h=(b-a)/(2*(int)(N[0]))
    for i in range(1,(int)(N[0])+1):
        x=a+(2*i-1)*h
        s1=s1+f(x)
    for i in range(1,(int)(N[0])):
        x=a+(2*i-1)*h
        s2=s2+f(x)
    return((f(a)+4.0*s1+2.0*s2+f(b))*h/3.0)
