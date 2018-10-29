from numpy import random, sqrt, log, sin, cos, pi
from pylab import show,hist,subplot,figure

#Transformation Function
def gaussian(u1,u2):
	z1=sqrt(-2*log(u1))*cos(2*pi*u2)
	z2=sqrt(-2*log(u1))*sin(2*pi*u2)
	return z1,z2

#Uniformly Distributed Values between 0 and 1
u1=random.rand(100000)
u2=random.rand(100000)

#Transformation Function
def gaussian(u1,u2):
	z1=sqrt(-2*log(u1))*cos(2*pi*u2)
	z2=sqrt(-2*log(u1))*sin(2*pi*u2)
	return z1,z2

#Uniformly Distributed Values between 0 and 1
u1=random.rand(100000)
u2=random.rand(100000)

#Run the Transformation
z1,z2=gaussian(u1,u2)

#Plotting the Values Before and After the Transformation
figure()
# the first row of graphs
subplot(221)
hist(u1)     # contains the histograms of u1 and u2 
subplot(222)
hist(u2)
# the second contains
subplot(223)
hist(z1)     # the histograms of z1 and z2
subplot(224)
hist(z2)
show()
