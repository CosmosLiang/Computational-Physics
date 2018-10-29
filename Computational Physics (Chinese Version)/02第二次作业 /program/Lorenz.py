"""

`\textcolor{darkgreen}{3阶Runge-Kutta法求解Lorenz混沌因子方程}`

"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#`\textcolor{darkgreen}{定义步数}`
n=1000
#`\textcolor{darkgreen}{变量初始化}`
x=np.zeros(n+1,dtype='float64')
y=np.zeros(n+1,dtype='float64')
z=np.zeros(n+1,dtype='float64')
#`\textcolor{darkgreen}{常微分方程}`
def f1(x,y,z):
    return(10.0*(y-x))
def f2(x,y,z):
    return(x*(28.0-z)-y)
def f3(x,y,z):
    return(x*y-8.0*z/3)
#`\textcolor{darkgreen}{3阶Runge-Kutta法}`
def Runge_Kutta(x0,y0,z0,n,x,y,z):
    x[0]=x0;y[0]=y0;z[0]=z0;h=10/n;i=0
    while(i!=n):
        k1=f1(x[i],y[i],z[i])
        l1=f2(x[i],y[i],z[i])
        m1=f3(x[i],y[i],z[i])
        k2=f1(x[i]+h/2.0,y[i]+h*k1/2.0,z[i]+h*k1/2.0)
        l2=f2(x[i]+h/2.0,y[i]+h*l1/2.0,z[i]+h*l1/2.0)
        m2=f3(x[i]+h/2.0,y[i]+h*m1/2.0,z[i]+h*m1/2.0)
        k3=f1(x[i]+h,y[i]-h*k1+2.0*h*k2,z[i]-h*k1+2.0*h*k2)
        l3=f2(x[i]+h,y[i]-h*l1+2.0*h*l2,z[i]-h*l1+2.0*h*l2)
        m3=f3(x[i]+h,y[i]-h*m1+2.0*h*m2,z[i]-h*m1+2.0*h*m2)
        x[i+1]=x[i]+h*(k1+4.0*k2+k3)/6.0
        y[i+1]=y[i]+h*(l1+4.0*l2+l3)/6.0
        z[i+1]=z[i]+h*(m1+4.0*m2+m3)/6.0
        i=i+1
#`\textcolor{darkgreen}{主函数}`
Runge_Kutta(5.0,20.0,-10.0,n,x,y,z)
#`\textcolor{darkgreen}{绘图}`
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x,y,z,c='b')
plt.show()
