name="Pra rk2"
import math as m
def pra_rk2(fun, x0, y0, xn, n):
    h=(xn - x0)/n
    for i in range (1,n+1):
        k1 = h * fun(x0, y0)
        k2 = h * fun(x0+h/2,y0+k1/2)
        ynew = y0 + (k1+k2)/2
        print("x= %.4f; y=%.4f; ynew =%.4f"%(x0,y0, ynew))
        x0=x0+h
        y0=ynew
        print("xn=%.4f; yn=%.4f"%(xn, ynew))

pra_rk2(lambda x,y: 2-x*y,5,2,5.1,10)