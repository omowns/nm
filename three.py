import math as m
def st_sam(gun,dgun,x1,acc,maxitr):
    while abs(dgun(x1))>1:
        print("wrong initial guess, enter new value of x1")
        x1 = float(input("enter value of x1"))
    for itr in range(maxitr):
        x0 = gun(x1)
        if abs(x0-x1)<acc:
            break;
        else:
            x1 = x0
    print("Root of the equation = %.4f"%x0)
st_sam(lambda x: m.exp(x)*m.cos(x)-1.4+x, lambda x: -
m.exp(x)*m.sin(x)+m.exp(x)*m.cos(x)+1,1,0.0001,100)