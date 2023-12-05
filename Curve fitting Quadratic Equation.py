import numpy as np
def st_qcf(x,y):
    x = x.astype (float)
    y = y.astype(float)
    A = np.array ([ [len(x),sum(x),sum(x*x)],
                    [sum(x),sum(x*x),sum(x*x*x)],
                    [sum(x*x),sum(x*x*x),sum(x*x*x*x)]])
    B = np.array([[sum(y)],
                    [sum(x*y)],
                    [sum(x*x*y)]])
    C = np.linalg.solve(A,B)
    print("y = %.4f + % .4f * x + %.4f x*x "%(C[0],C[1],C[2]))
    
st_qcf(np.array([6,7,7,8,8,8,9,9,10]),np.array([5,5,4,5,4,3,4,3,3]))