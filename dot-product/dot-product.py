import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    x=np.array(x)
    y=np.array(y)

    if x.shape != y.shape:
        raise ValueError
   
    return float(np.sum(x*y))