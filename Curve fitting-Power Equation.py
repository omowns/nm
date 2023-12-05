import numpy as np
import math as m
def st_pe(x,y):
    x=x.astype(float)
    y=y.astype(float)
    n=len(x)
    X=np.log(x)
    Y=np.log(y)
    A=np.array([[n,sum(X)],[sum(X),sum(X*X)]])
    C=np.array([[sum(Y)],[sum(X*Y)]])
    B=np.linalg.solve(A,C)
    alpha= m.exp(B[0])
    beta= B[1]
    print("y=%.4f*x^%.4f"%(alpha,beta))

st_pe(np.array([61,26,7,2.6]),np.array([350,400,50,600]))