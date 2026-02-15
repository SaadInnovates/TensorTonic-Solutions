import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        matrix=np.asarray(matrix,dtype=complex)
    except:
        return None
        
    if matrix.ndim !=2:
        return None
    
    (r,c)=matrix.shape

    if r!=c:
        return None


    try:
        eigvals=np.linalg.eigvals(matrix)
        
    except np.linalg.LinAlgError:
        return None

    eigvals = np.where(abs(eigvals.real)<1e-10, eigvals.imag*1j, eigvals)
    eigvals = np.where(abs(eigvals.imag)<1e-10, eigvals.real, eigvals)
    
    idx = np.lexsort((eigvals.imag, eigvals.real))
    eigvals_sorted = eigvals[idx]
    return eigvals_sorted
    
    
    