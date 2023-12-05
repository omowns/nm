import numpy as np
import math as m
def st_nfdi(x,y,xr):
    x = x.astype(float)
    y = y.astype(float)
    n = len(x)
    delta = np.zeros((n-1,n-1))
    for j in range(n-1):
        for i in range((n-1)-j):
            if j == 0:
                delta[i,j] = y[i+1] - y[i]
            else:
                delta[i,j] = delta[i+1,j-1] - delta[i,j-1]
    h = x[1] - x[0]
    u = (xr - x[0])/h
    term = 0
    mult = 1
    for j in range(n-1):
        mult = mult * (u-j)
        term = term + delta[0,j] / m.factorial(j+1) * mult
    yr = y[0]+term
    print("y at x = %.4f is equal to %.4f" %(xr,yr))
    
st_nfdi(np.array([100,150,200,250,300,350,400]),np.array([10.63,13.03,15.04,16.81,18.42,19.90,21.27]),160)