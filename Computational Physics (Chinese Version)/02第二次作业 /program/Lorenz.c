#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define N 100000
//Ordinary Differential Equation
double f1(double x,double y,double z)
{
    return(10.0*(y-x));
}
double f2(double x,double y,double z)
{
    return(x*(28.0-z)-y);
}
double f3(double x,double y,double z)
{
    return(x*y-8.0/3*z);
}
int main()
{
    double f1(double x,double y,double z);
    double f2(double x,double y,double z);
    double f3(double x,double y,double z);
	int RungeKutta(double x0,double y0,double z0,
int n,double *x,double *y,double *z,double (*f1)
(double,double,double),double (*f2)(double,double
,double),double (*f3)(double,double,double));
    int i;
	FILE *fp;
	fp = fopen("Lorenz.txt", "w");
    double x0=5.0,y0=20.0,z0=-10.0,x[N],y[N],z[N];
	RungeKutta(x0,y0,z0,N,x,y,z,f1,f2,f3);
	for(int i=0;i<N;i++)
	{
		fprintf(fp,"%lf,%lf,%lf\n", x[i],y[i],z[i]);
	}
	fclose(fp);
    return 0;
}
//3 Order Runge Kutta
int RungeKutta(double x0,double y0,double z0,
int n,double *x,double *y,double *z,double (*f1)
(double,double,double),double (*f2)(double,double
,double),double (*f3)(double,double,double))
{
	double h=0.001,k1,k2,k3,l1,l2,l3,m1,m2,m3;
	int i;
	x[0]=x0;
	y[0]=y0;
	z[0]=z0;
		for(i=0;i<n;i++)
		{
			k1=f1(x[i],y[i],z[i]);
			l1=f2(x[i],y[i],z[i]);
			m1=f3(x[i],y[i],z[i]);
			k2=f1(x[i]+h/2.0,y[i]+h*k1/2.0,z[i]
+h*k1/2.0);
			l2=f2(x[i]+h/2.0,y[i]+h*l1/2.0,z[i]
+h*l1/2.0);
			m2=f3(x[i]+h/2.0,y[i]+h*l1/2.0,z[i]
+h*l1/2.0);
			k3=f1(x[i]+h,y[i]-h*k1+2.0*h*k2,z[i]
-h*k1+2.0*h*k2);
			l3=f2(x[i]+h,y[i]-h*l1+2.0*h*l2,z[i]
-h*l1+2.0*h*l2);
			m3=f3(x[i]+h,y[i]-h*l1+2.0*h*l2,z[i]
-h*l1+2.0*h*l2);
			x[i+1]=x[i]+h*(k1+4.0*k2+k3)/6.0;
			y[i+1]=y[i]+h*(l1+4.0*l2+l3)/6.0;
			z[i+1]=z[i]+h*(m1+4.0*m2+m3)/6.0;
		}
}

