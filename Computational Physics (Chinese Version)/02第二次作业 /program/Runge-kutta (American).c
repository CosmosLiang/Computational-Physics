#include<stdio.h>
#include<stdlib.h>
#include<math.h>
//Step
#define N 10000
//Constant
#define a 1.733691835*pow(10,22)
#define b 1.295934646*pow(10,-11)
//Boundary
#define xx0 0.0
#define xxf 2*3.1415926535897932384626
#define r0 149500000000
int RungeKutta(double x0,double xf,double y0
,int n,double *x,double *y,int style,double 
(*f)(double,double))
{
	double h=(xf-x0)/n,k1,k2,k3,k4;
	int i;
	x[0]=x0;
	y[0]=y0;
	switch(style)
	{
	case 2:
	//2 Order Runge-Kutta
	for(i=0;i<n;i++)
	{
	x[i+1]=x[i]+h;
	k1=f(x[i],y[i]);
	k2=f(x[i]+h/2,y[i]+h*k1/2);
	y[i+1]=y[i]+h*k2;
	}
	break;
	case 3:
	//3 Order Runge-Kutta
	for(i=0;i<n;i++)
	{
	x[i+1]=x[i]+h;
	k1=f(x[i],y[i]);
	k2=f(x[i]+h/2,y[i]+h*k1/2);
	k3=f(x[i]+h,y[i]-h*k1+2*h*k2);
	y[i+1]=y[i]+h*(k1+4*k2+k3)/6;
	}
	break;
	case 4:
	//4 Order Runge-Kutta
	for(i=0;i<n;i++)
	{
	x[i+1]=x[i]+h;
	k1=f(x[i],y[i]);
	k2=f(x[i]+h/2,y[i]+h*k1/2);
	k3=f(x[i]+h/2,y[i]+h*k2/2);
	k4=f(x[i]+h,y[i]+h*k3);
	y[i+1]=y[i]+h*(k1+2*k2+2*k3+k4)/6;
	}
	break;
	default:
	return 0;
	}
	return 1;
}
//Ordinary Differerial Equation
double f(double x,double y)
{
	return(sqrt(a*pow(x,4)+b*pow(x,3)-x*x));
}
//Main Function
int main()
{
	int i;
	double x[N],y[N];
	double f(double x,double y);
	int RungeKutta(double x0,double xf,double 
y0,int n,double *x,double *y,int style,double 
(*f)(double,double));
	RungeKutta(xx0,xxf,r0,N,x,y,2,f);
	for(int i=0;i<N;i++)
	printf("x[%d]=%f,y[%d]=%f\n",i,x[i],i,y[i]);
	RungeKutta(xx0,xxf,r0,N,x,y,3,f);
	for(i=0;i<N;i++)
	printf("x[%d]=%f,y[%d]=%f\n",i,x[i],i,y[i]);
	RungeKutta(xx0,xxf,r0,N,x,y,4,f);
	for(i=0;i<N;i++)
	printf("x[%d]=%f,y[%d]=%f\n",i,x[i],i,y[i]);
	return 1;
}
