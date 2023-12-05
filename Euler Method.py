import math as m
def st_em(fun,x0,y0,xn,n):
    h=(xn-x0)/n
    for i in range(1,n+1):
        ynew=y0+h*fun(x0,y0)
        x0=x0+h
        y0=ynew
        print("x=%.4f"%x0,"y=%.4f"%y0)
        
st_em(lambda x,y:m.sqrt(x+m.sqrt(y)),2,4,2.5,10)