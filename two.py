import math as m
def st_nrm(fun,dfun,ddfun,x1,acc,maxitr):
    while abs(fun(x1)*ddfun(x1)/dfun(x1)**2)>1:
        print("initial guess is wrong, enter new value")
        x1 = float(input("enter value of x1 = "))
    for itr in range(maxitr):
        x0 = x1 - (fun(x1)/dfun(x1))
        if abs(x1-x0)<acc:
            break;
        else:
            x1 = x0
    print("the roots of the equation = %.4f"%x0)
st_nrm(lambda x: x**3-5*x+3,lambda x:3*x**2-5,lambda x:6*x,0,0.0001,10)