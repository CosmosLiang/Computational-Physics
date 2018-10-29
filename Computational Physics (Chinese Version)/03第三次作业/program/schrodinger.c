#include<stdio.h>
#include<math.h>
double V1(double x);
double F(int n,double x0,double y0,double xn,double yn,double xm,double K[n+1],double k); 
double Fa(int n,double x0,double y0,double xn,double yn,double xm,double K[n+1],double k); 
double VTarget_2(int n,double x0,double y0,double xn,double yn,double xm,double K[n+1],
double k); 
int main()
{
	int n=500,i;
	double m0=9.108e-31,ml=0.916*m0,V0=1.602e-20,a=3e-9,h1=1.055e-34/pow(m0*V0,1.0/2)/a,
l=35e-9; 
	double x0=0,xn=l/a,y0=0,yn=0,k=-10,x,h,tx0,xm,d,t;
	double v1[n+1];
	t=21.614; 
	x=x0;
	h=(xn-x0)/n;
	for(i=0;i<=n;i++)
	{
		v1[i]=-V1(x)*t;
		x=x+h;
	}
	d=0.01;
	tx0=x0;
	xm=tx0+50*d;
	VTarget_2(n,x0,y0,xn,yn,xm,v1,k*t); 
	return 0;
}
double V1(double x)
{
	double v;
	v=(3.0/35*x-1)*10;
	return v;
}
double VTarget_2(int n,double x0,double y0,double xn,double yn,double xm,double K[n+1],
double k)
{
	int i,l;
	double ty0,ty1,tyn,tyn1,d,x,h,f1,f2,tf,tk,ys,yb,a,Sum,t;
	double f[n-3];
	FILE *fp;
	d=0.1;
	h=(xn-x0)/n;
for(l=0;k<=0;l++)
{
	tk=k+d;
	f1=1;
	for(i=1;fabs(f1)>=0.000001;i++)	 
	{
		f1=F(n,x0,y0,xn,yn,xm,K,k); 
		f2=F(n,x0,y0,xn,yn,xm,K,tk); 
		if(f2*f1>=0) 
		{
			f1=f2;
			k=tk;
			tk=tk+d;
			f2=F(n,x0,y0,xn,yn,xm,K,tk);
		}
		else 
		{
			tf=F(n,x0,y0,xn,yn,xm,K,(tk+k)/2);
			if(tf*f1>=0)
			{
				k=(tk+k)/2;
				t=k;
				f1=tf;
			}
			else
			{
				tk=(tk+k)/2;
				t=tk;
				f2=tf;
			}
		}
		if(fabs(f1-f2)>=1000000)
		{
			k=k+d;
			tk=tk+d;
		}
	}
		a=Fa(n,x0,y0,xn,yn,xm,K,t);
		x=x0+h;
		ty0=y0;
		ty1=y0+0.001;
		tyn=yn;
		tyn1=yn+0.001;
		Sum=1.0/3*ty0*h+4.0/3*ty1*h;
		for(i=1;x<=xm;i++)
		{
			ys=(-(1+pow(h,2)*(t+K[i-1])/12)*ty0+2*(1-5*pow(h,2)*(t+K[i])/12)*ty1)/(1+pow
(h,2)*(t+K[i+1])/12);
			ty0=ty1;
			ty1=ys;
			f[i-1]=ys;
			if(i%2==0)
			{
				Sum=Sum+2.0/3*ys*h;
			}
			else
			{
				Sum=Sum+4.0/3*ys*h;
			}
			x=x+h;
		}
		x=xn-h;
		Sum=Sum+1.0/3*tyn*h+4.0/3*tyn1*h;
		for(i=n-1;x>xm;i--)
		{
			yb=(-(1+pow(h,2)*(t+K[i+1])/12)*tyn+2*(1-5*pow(h,2)*(t+K[i])/12)*tyn1)/(1+pow
(h,2)*(t+K[i-1])/12); 
			tyn=tyn1;
			tyn1=yb;
			f[i-1]=yb*a;
			if(i%2==0)
			{
				Sum=Sum+2.0/3*yb*a*h;
			}
			else
			{
				Sum=Sum+4.0/3*yb*a*h;
			}
			x=x-h;
		}
		printf("%lf,%lf\n",a*yb,ys);

		x=x0+h;
		for(i=0;i<=n-2;i++)
		{
			x=x+h;
			fp=fopen("wavefuction.txt","a");
			fprintf(fp,"%lf,%lf,%lf\n",x,f[i]/Sum,t/21.614);
			fclose(fp);
		}
		k=tk;
}
	return 0;
}
double F(int n,double x0,double y0,double xn,double yn,double xm,double K[n+1],double k)
{
	double h=(xn-x0)/n,y1=y0+0.001,yn1=yn+0.001,ys,ss,yb,sb,a,x=x0+h;
	int i;
	for(i=1;x<=xm;i++)
	{
		ys=(-(1+pow(h,2)*(k+K[i-1])/12)*y0+2*(1-5*pow(h,2)*(k+K[i])/12)*y1)/(1+pow(h,2)*
(k+K[i+1])/12);
		ss=1.0/2/h*(-ys+4*y1-3*y0);
		y0=y1;
		y1=ys;
		x=x+h;
	}
	x=xn-h;
	for(i=n-1;x>xm;i--)
	{
		yb=(-(1+pow(h,2)*(k+K[i+1])/12)*yn+2*(1-5*pow(h,2)*(k+K[i])/12)*yn1)/(1+pow(h,2)*
(k+K[i-1])/12);
		sb=1.0/2/h*(-yn+4*yn1-3*yb);
		yn=yn1;
		yn1=yb;
		x=x-h;
	}
	a=ys/yb;
	sb=sb*a;
	return (sb-ss);
}
double Fa(int n,double x0,double y0,double xn,double yn,double xm,double K[n+1],double k)
{
	double h=(xn-x0)/n,y1=y0+0.001,yn1=yn+0.001,ys,yb,a,x=x0+h;
	int i;
	for(i=1;x<=xm;i++)
	{
		ys=(-(1+pow(h,2)*(k+K[i-1])/12)*y0+2*(1-5*pow(h,2)*(k+K[i])/12)*y1)/(1+pow(h,2)*
(k+K[i+1])/12);
		y0=y1;
		y1=ys;
		x=x+h;
	}
	x=xn-h;
	for(i=n-1;x>xm;i--)
	{
		yb=(-(1+pow(h,2)*(k+K[i+1])/12)*yn+2*(1-5*pow(h,2)*(k+K[i])/12)*yn1)/(1+pow(h,2)*
(k+K[i-1])/12);
		yn=yn1;
		yn1=yb;
		x=x-h;
	}
	a=ys/yb;
	return a;
}
