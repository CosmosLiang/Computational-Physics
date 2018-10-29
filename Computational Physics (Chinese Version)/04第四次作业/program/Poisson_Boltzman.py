'''Use iterative method to find the solution of Possion-Boltzman
equation with the first type of boundary Condition'''
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import sympy
'''Input Parameter'''
N=30000
a=0;b=300
epsilon2=0.1
Z=1.0
mu=1.0
dx=(b-a)/N
'''Functions'''
def sech(x):
	return(sympy.cosh(x)**(-1))
'''Two order difference formula'''
#tridiagonal matrices
a=[];b=[];c=[]
d=np.ones(N,dtype='float64')
for i in range(N+1):
	a.append(d[i-1]/(dx*dx))
	b.append(-2*d[i-1]/(dx*dx))
	c.append(d[i-1]/(dx*dx))
a[0]=0;c[N]=0
#discrete of right side
Ni=[]
def ni(x):
	u0=1.0
	x0=100
	epsilon=double(epsilon2**(0.5))
	return(double(1+3*epsilon**(2)*u0*sech(epsilon*u0**(0.5)*(x-x0)/2)**(2)))
for i in range(N+1):
	Ni.append(ni((i+1)*dx))
'''Iterative'''
gam=np.zeros(N+1,dtype='float64')
phi=np.zeros(N+1,dtype='float64')
f=np.zeros(N+1,dtype='float64')
tolx=0.0001
while tolx>=0.0001:
	tolx=0
	p=double(b[0])-dx*dx*exp(double(f[0]))
	phi[0]=dx*dx*(exp(f[0])*(1-f[0])-Ni[0])/p
	j=0
	while j<N:
		gam[j]=c[j]/p
		p=double(b[j+1])-dx*dx*exp(double(f[j+1]))-double(a[j])*double(gam[j])
		phi[j+1]=(dx*dx*(exp(f[j+1])*(1-f[j+1])-Ni[j+1])-a[j]*phi[j]/p)
		j=j+1
	j=N
	while j>0:
		err=f[j]
		phi[j-1]=(phi[j-1]-phi[j]*gam[j])
		f[j]=phi[j]
		err=abs(err-f[j])
		if err>=tolx:
			tolx=err
		j=j-1
	f[0]=phi[0]
x=[]
for i in range(N+1):
	x.append(i*dx)
fig=plt.figure()
ax=fig.add_subplot(111)
ax.grid()
plt.plot(x,phi)
plt.xlabel('x')
plt.ylabel('$\psi(x) $',fontsize=18)
plt.title('Solution to Poisson Boltzman Equation')
plt.show()
