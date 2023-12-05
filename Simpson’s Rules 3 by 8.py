import math as m
def st_S38(fun,x0,xn,n):
    h=(xn-x0)/n
    y0=fun(x0)
    yn=fun(xn)
    yr=0
    ym3=0
    for i in range (1,n,1):
        yr = yr + fun(x0 + i * h)
    for j in range (3,n,3):
        ym3 = ym3 + fun(x0 + j * h)
    I= (3/8) * h * (y0 + yn + 3 * (yr - ym3) + 2 * ym3)
    print("Integration : %0.4f"%I)

st_S13(lambda x: 1/(1+x*x),0,6,6)
