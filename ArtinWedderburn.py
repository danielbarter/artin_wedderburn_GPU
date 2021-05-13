import cupy as cp
import cupyx.scipy.sparse as sparse
from PermutationEnumerator import PermutationEnumerator

class Algebra:
    def __init__(
            self,
            dimension, # int
            left_multiplication_matrices, # cupy sparse matrices
            unit, # cupy dense vector
            star # cupy sparse matrix
    ):

        # dimension of algebra
        # we denote the basis vectors as e_1, e_2, ...., e_dimension
        self.dimension = dimension

        # list of matrices
        # jth column of ith matrix is e_i e_j
        self.left_multiplication_matrices = left_multiplication_matrices

        # useful optimization for implementing multiply
        self.multiplication_matrix = sparse.hstack(left_multiplication_matrices)

        # unit of algebra. Dense cupy array
        self.unit = unit



def symmetric_group(n):
    pe = PermutationEnumerator(n)
