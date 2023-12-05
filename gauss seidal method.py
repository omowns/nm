import numpy as np
def st_gsm(a,d,maxitr):
    a=a.astype(float)
    d=d.astype(float)
    n=len(d)
    x= np.zeros(n)
    for itr in range(maxitr):
        for i in range(n):
            temp=0
        for j in range(n):
            if j!=i:
                temp=temp+a[i,j]*x[j]
            x[i]=(d[i]-temp)/a[i,i]
        for i in range(n):
            print("x(%i): %.4f"%(i,x[i]))
        print(" \n")
st_gsm(np.array([[4,1,2,3],[3,4,1,2],[2,3,4,1],[1,2,3,4]]),np.array([40
,40,40,40]),2)