import numpy as np
def gaussian_elimination(A,b):
	n=len(A)
	x=np.ones([n,1])
	b=b.reshape(n,1)
	A_b=np.hstack((A,b))
	for i in range(n):
		for j in range(i+1,n):
			A_b[j]=A_b[j]-A_b[i]*(A_b[j][i]/A_b[i][i])
	for i in range(n-1,-1,-1):
		sum=A_b[i][n]
		for j in range(i+1,n):
			sum=sum-A_b[i][j]*x[j]
		x[i]=sum/A_b[i][i]
	return x.T[0]
def jacobi(A,b):
	n=len(A)
	x=np.ones([n,1])
	b=b.reshape(n,1)
	B=np.zeros([n,n])
	D=np.zeros([n,n])
	d=np.ones([n,1])
	B=A.copy()
	for i in range(n):
		B[i,i]=0.0
		D[i,i]=A[i,i].copy()
	B=np.dot(-np.linalg.inv(D),B)
	d=np.dot(np.linalg.inv(D),b)
	x1=x
	x2=np.dot(B,x)+d
	while(np.linalg.norm(x1-x2,np.inf)>10e-10):
		x1=x2
		x2=np.dot(B,x1)+d
	return x2.T[0]
def gauss_seidel(A,b):
	n=len(A)
	x=np.ones([n,1])
	b=b.reshape(n,1)
	B=np.tril(A)
	U=np.triu(A,k=1)
	G=-np.dot(np.linalg.inv(B),U)
	d=np.dot(np.linalg.inv(B),b)
	x1=x
	x2=np.dot(G,x)+d
	while(np.linalg.norm(x1-x2,np.inf)>10e-10):
		x1=x2
		x2=np.dot(G,x1)+d
	return x1.T[0]
def sor(A,b):
	w=1.15
	n=len(A)
	x=np.ones([n,1])
	b=b.reshape(n,1)
	L=np.tril(A,k=-1)
	U=np.triu(A,k=1)
	D=np.zeros([n,n])
	for i in range(n):
		D[i,i]=A[i,i].copy()
	x1=x
	x2=np.dot(np.dot(np.linalg.inv(D+w*L),((1-w)*D-w*U)),x)+w*np.dot(np.linalg.
inv(D+w*L),b)
	while(np.linalg.norm(x1-x2,np.inf)>10e-10):
		x1=x2
		x2=np.dot(np.dot(np.linalg.inv(D+w*L),((1-w)*D-w*U)),x1)+w*np.dot(np.linalg.
inv(D+w*L),b)
	return x1.T[0]
