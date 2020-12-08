from numpy import kron, outer, eye
from itertools import product

def revmat(M):
    d = M.shape[0]//2
    return M if d==1 else sum([kron(revmat(M[i*d:(i+1)*d, j*d:(j+1)*d]), outer(eye(2)[i], eye(2)[j])) for (i, j) in product([0, 1], repeat = 2)])