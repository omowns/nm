import numpy as np
def st_li(x,y,xr):
    x = x.astype(float)
    y = y.astype(float)
    n = len(x)
    yr = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L = L *((xr - x[j])/(x[i]-x[j]))
            yr = yr + y[i] * L
    print("y at x = %.4f is equal to %.4f"%(xr,yr))
    
st_li(np.array([100,150,200,250,300,350,400]),np.array([10.63,13.03,15.04,16.81,18.42,19.90,21.27]),160)