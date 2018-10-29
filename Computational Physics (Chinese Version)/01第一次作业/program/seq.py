"""

`\textcolor{darkgreen}{数值求解方程}`

"""
import numpy as np
#`\textcolor{darkgreen}{初始猜测位置}`
a=1.5;b=2.0
#`\textcolor{darkgreen}{可容忍误差}`
tolx=[0.00000000001]
#`\textcolor{darkgreen}{求解方程对应函数}`
def f(x):
    return(-0.40705+1.0/x*np.exp(-0.1*x)*np.cos(0.1*x))
#`\textcolor{darkgreen}{求解方程对应函数的导数}`
def dif(x):
    return(-((np.exp(-0.1*x)*np.cos(0.1*x))/(x*x))-(0.1*np.exp(-0.1*x)*np.sin(0.1*x))/
x-(0.1*np.exp(-0.1*x)*np.cos(0.1*x))/x)
#`\textcolor{darkgreen}{二分法}`
def dichotomy(f0,a,b):
	i=0#`\textcolor{darkgreen}{收敛步数初始化}`
	while(abs(b-a)>tolx[0]):
		i=i+1
		if(f0((a+b)/2.0)==0):
			a=(a+b)/2.0
		else:
			if(f0((a+b)/2.0)*f(a)<0):
				b=(a+b)/2.0
			if(f0((a+b)/2.0)*f(b)<0):
				a=(a+b)/2.0
	return(i,a,a-1.97678815877)
#`\textcolor{darkgreen}{Newton法}`
def newton(f0,dif0,a,b):
	i=0#`\textcolor{darkgreen}{收敛步数初始化}`
	while(abs(a-1.97678815877)>tolx[0]):
		i=i+1
		a=a-f0(a)/dif0(a)
	return(i,a,a-1.97678815877)
#`\textcolor{darkgreen}{弦切法}`
def stringcut(f0,a,b):
	i=0#`\textcolor{darkgreen}{收敛步数初始化}`
	c=b-f0(b)*((b-a)/(f0(b)-f0(a)))
	while(abs(c-a)>tolx[0]):
		i=i+1
		c=b-f0(b)*((b-a)/(f0(b)-f0(a)))
		a=b
		b=c
	return(i,c,c-1.97678815877)
#`\textcolor{darkgreen}{主函数}`
print(dichotomy(f,a,b))
print(newton(f,dif,a,b))
print(stringcut(f,a,b))
