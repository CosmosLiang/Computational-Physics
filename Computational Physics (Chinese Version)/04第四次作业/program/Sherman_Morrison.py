'''
use Sherman-Morrison Formula and Thomas Method to solve cyclic tridiagonal linear
equation
'''
import numpy as np
# Thomas Method for soling tridiagonal linear equation Ax=r
# parameter: a,b,c,d are list-like of same length
# b: main diagonal of matrix A
# a: main diagonal below of matrix A
# c: main diagonal upper of matrix A
# d: Ax=d
# return: x(type=list), the solution of Ax=r
def TDMA(a,b,c,d):
    try:
        n = len(d)    # order of tridiagonal square matrix
# use a,b,c to create matrix A, which is not necessary in the algorithm
        A = np.array([[0]*n]*n, dtype='float64')
        for i in range(n):
            A[i,i] = b[i]
            if i > 0:
                A[i, i-1] = a[i]
            if i < n-1:
                A[i, i+1] = c[i]
        c_1 = [0]*n# new list of modified coefficients
        d_1 = [0]*n
        for i in range(n):
            if not i:
                c_1[i] = c[i]/b[i]
                d_1[i] = d[i]/b[i]
            else:
                c_1[i] = c[i]/(b[i]-c_1[i-1]*a[i])
                d_1[i] = (d[i]-d_1[i-1]*a[i])/(b[i]-c_1[i-1] * a[i])
        x = [0]*n # x: solution of Ax=r
        for i in range(n-1, -1, -1):
            if i == n-1:
                x[i] = d_1[i]
            else:
                x[i] = d_1[i]-c_1[i]*x[i+1]
        x = [round(_, 4) for _ in x]
        return(x)
    except Exception as e:
        return(e)
def Cyclic_Tridiagnoal_Linear_Equation(a,b,c,d):
    try:
        n = len(d)# use a,b,c to create cyclic tridiagonal matrix A
        A = np.array([[0] * n] * n, dtype='float64')
        for i in range(n):
            A[i, i] = b[i]
            if i > 0:
                A[i, i - 1] = a[i]
            if i < n - 1:
                A[i, i + 1] = c[i]
        A[0, n - 1] = a[0]
        A[n - 1, 0] = c[n - 1]
        gamma = 1 # gamma can be set freely
        u = [gamma] + [0] * (n - 2) + [c[n - 1]]
        v = [1] + [0] * (n - 2) + [a[0] / gamma]
        # modify the coefficient to form A'
        b[0] -= gamma
        b[n-1] -= a[0] * c[n-1] / gamma
        a[0] = 0
        c[n - 1] = 0
        # solve A'y=d, A'z=u by using Thomas Method
        y = np.array(TDMA(a, b, c, d))
        z = np.array(TDMA(a, b, c, u))
        x = y - (np.dot(np.array(v), y)) / (1 + np.dot(np.array(v), z)) * z
        x = [round(_,3) for _ in x]
        return(x)
    except Exception as e:
        return(e)
def main():
    a = [2, 1, 1, 1, 1]
    b = [4, 4, 4, 4, 4]
    c = [1, 1, 1, 1, 3]
    d = [7, 6, 6, 6, 8]
    x = Cyclic_Tridiagnoal_Linear_Equation(a,b,c,d)
    print('The solution is %s'%x)
main()
