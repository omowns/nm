import numpy as np
def st_slcf(x,y):
    x = x.astype (float)
    y = y.astype(float)
    A = np.array([ [len(x) , sum(x)],
                    [sum(x) , sum(x*x)]])
    B = np.array([ [sum(y)],
                    [sum(x*y)]])
    C = np.linalg .solve(A,B)
    print("y =%.4f + %.4f *x"%(C[0],C[1]))
    
st_slcf(np.array([6,7,7,8,8,8,9,9,10]),np.array([5,5,4,5,4,3,4,3,3]))