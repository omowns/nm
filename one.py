import math as m
def st_bsm(fun,x1,x2,acc,maxitr):
  while fun(x1)*fun(x2)>0:
    print("Intial guesses are wrong, enter new values ")
    x1 = float(input("Enter the value of x1 = "))
    x2 = float(input("Enter the value of x2 = "))
  for itr in range(maxitr):
    x0 = (x1+x2)/2
    if abs(x0-x1)<acc:
      break;
    if fun(x0)*fun(x1)<0:
      x1 = x1
      x2 = x0
    elif fun(x0)*fun(x1)>0:
      x1 = x0
      x2 = x2
      print("The roots of the equation : %.4f"%x0)