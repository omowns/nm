import numpy as np
def st_gem(a,d):
    a = a.astype(float)
    d = d.astype(float)
    n = len(d)
    for i in range(n):
        for k in range(i+1,n):
            fact = a[k,i]/a[i,i]
            for j in range (n):
                a[k,j]-fact*a[i,j]
                d[k] = d[k]-fact*d[i]
    x = np .zeros(n)
    for i in range (n-1,-1,-1):
        temp = 0
        for j in range (i+1,n):
            temp = temp + a[i,j]*x[j]
        x[i] = (d[i]-temp)/ a[i,i]
        print ("x(%i)= %.4f"%(i,x[i]))
st_gem(np.array ([[4,1,2,3],[3,4,1,2],[2,3,4,1],[1,2,3,4]]),np.array
([40,40,40,40]))
