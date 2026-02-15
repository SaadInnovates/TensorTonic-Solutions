import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    A=np.array(a)
    B=np.array(b)
    dot_prod=A @ B
    A_magnitude=np.sqrt(np.sum(A**2))
    B_magnitude=np.sqrt(np.sum(B**2))

    if A_magnitude == 0 or B_magnitude == 0:
        return 0.0
    return dot_prod/(A_magnitude * B_magnitude)
    