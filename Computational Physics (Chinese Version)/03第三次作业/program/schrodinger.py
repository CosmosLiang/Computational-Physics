from numpy import *
import numpy as np
import matplotlib.pyplot as plt
#Input Parameter
E=[0.7]
#Constant
mass=0.916*9.10938215*power(10.0,-31.0)
e=1.602176487*power(10.0,-19.0)
c=3*power(10.0,-9.0)
pi=3.1415926535897932384626
hbar=6.62606896*power(10.0,-34.0)/(2*pi)
gamma=2.0*mass*c*c*e/(hbar*hbar)
#Parameter
amax=0.0
amin=-1.0
Tolerance=0.000001
delta=0.001
NL=0
NR=0
N=0
h=0.1
Width=35.0/3.0
Slope=3.0/35.0
#Fuction Potential Function V(x)
def V(x):
	return(Slope*x)
#Fuction K2_Fuction
def K2(x):
	return(gamma*(E[0]-V(x)))
#Function FindRoot
def FindRoot(x1,f):
	x2=35
	for i in range(0,10000000):
		x3=x2-f(x2)*((x2-x1)/(f(x2)-f(x1)))
		if abs(x3-x2)<0.0000001:
			break
		else:
			x1=x2
			x2=x3
	return(x3)
#Function FindTippingPoint
def FindTippingPoint(x,f):
    global x0,NL,NR,N
    x0=FindRoot(x,f)
    NL=abs(int(x0/delta))
    NR=abs(int((Width-x0)/delta))
    N=NL+NR
#Function Numerov
def Numerov(n,h,q,u,e):
	K2(Width*e)
	b=(h**2)/12.0
	for i in range(1,n-1):
		u[i+1]=(2*u[i]*(1-5.*b*q[i])-(1+b*q[i-1])*u[i-1])/(1+b*q[i+1])
#Function Difference
def Difference(e):
	global NL,NR,delta
	Numerov(NL,delta,qL,PsiLeft,e)
	Numerov(NR,delta,qR,PsiRight,e)
	f0=(PsiRight[NR-1]+PsiLeft[NL-1]-PsiRight[NR-2]-PsiLeft[NL-2])/(PsiRight[NR-1]*(delta))
	return(f0)
#Function Rescale
def Rescale(NL,NR):
	C=PsiRight[NR-1]/PsiLeft[NL-1]
	for i in range(0,NL-1):
		PsiLeft[i]=C*PsiLeft[i]
#Function Normalization
#Main Function
FindTippingPoint(1,K2)
q=zeros((N),double)
PsiLeft=zeros((NL+1),double);PsiRight=zeros((NR+1),double)
PsiLeft[0]=0.0;PsiRight[0]=0.0
PsiLeft[1]=0.000001;PsiRight[1]=0.000001
qL=zeros((N),double);qR=zeros((N),double)
for i in range(0,N-1):
       xLeft=i*delta
       xRight=Width-i*delta
       qL[i]=K2(xLeft)
       qR[i]=K2(xRight)
istep = 0
x1=arange(0,x0-delta,delta);x2=arange(Width-delta,x0,-delta)
print(len(PsiRight))
fig=plt.figure()
ax=fig.add_subplot(111)
ax.grid()
while abs(Difference(E[0]))>Tolerance:
	E[0]=(amin+amax)/2
	if Difference(E[0])*Difference(amax) < 0: amax = E[0]
	else: amin = E[0]
	Rescale(NL,NR)
	ax.clear()
	plt.text(8,2,'Energy= %10.4f'%(E[0]),fontsize=12)
	plt.plot(x1,PsiLeft[:-1])
	plt.plot(x2,PsiRight[:-1])
	plt.xlabel('x')
	plt.ylabel('$\psi(x) $',fontsize=18)
	plt.title('R & L Wavefunctions Matched at x = %10.1f'%(x0))
	istep = istep+1
	plt.pause(0.8)  # Pause to delay figures
plt.show()
print(E[0])
