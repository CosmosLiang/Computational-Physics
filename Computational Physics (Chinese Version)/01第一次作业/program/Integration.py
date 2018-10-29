"""

`\textcolor{darkgreen}{积分上下限发散的积分}`

"""
import numpy as np
#`\textcolor{darkgreen}{积分上下限}`
a1=0;b1=(0.5)**(1.0/3)
a2=0;b2=(0.5)**(2.0/3)
#`\textcolor{darkgreen}{积分步数}`
N=[1000]
#`\textcolor{darkgreen}{积分标准值}`
I0=2*3.1415926535897932384626/np.sqrt(3)
#`\textcolor{darkgreen}{第一部分被积函数}`
def f1(x):
	return(3*pow((1-x*x*x),-1.0/3))
#`\textcolor{darkgreen}{第二部分被积函数}`
def f2(x):
	return(3.0/2*pow(1-pow(x,3.0/2),-2.0/3))
#`\textcolor{darkgreen}{矩形法积分}`
def rectangle(f,a,b):
	I=0;x=a;h=(b-a)/(int)(N[0])
	for i in range((int)(N[0])):
		I=I+f(x)*h
		x=x+h
	return(I)
#`\textcolor{darkgreen}{梯形法积分}`
def trapezoid(f,a,b):
	I=0;x=a;h=(b-a)/(int)(N[0])
	for i in range((int)(N[0])):
		I=I+1.0/2*(f(x)+f(x+h))*h
		x=x+h
	return(I)
#`\textcolor{darkgreen}{Simpson法积分}`
def simpson(f,a,b):
	h=(b-a)/(2*(int)(N[0]));s1=0.0;s2=0.0
	for i in range(1,(int)(N[0])+1):
		x=a+(2*i-1)*h
		s1=s1+f(x)
	for i in range(1,(int)(N[0])):
		x=a+2*i*h
		s2=s2+f(x)
	return((f(a)+4.0*s1+2.0*s2+f(b))*h/3.0)
#`\textcolor{darkgreen}{主函数}`
I1=rectangle(f1,a1,b1)+rectangle(f2,a2,b2)#`\textcolor{darkgreen}{矩形法求解}`
I2=trapezoid(f1,a1,b1)+trapezoid(f2,a2,b2)#`\textcolor{darkgreen}{梯形法求解}`
I3=simpson(f1,a1,b1)+simpson(f2,a2,b2)#`\textcolor{darkgreen}{Simpson法求解}`
#`\textcolor{darkgreen}{输出结果}`
print(I1,I1-I0,'\n')
print(I2,I2-I0,'\n')
print(I3,I3-I0,'\n')
