import cupy as cp
import cupyx.scipy.sparse as sparse
from math import factorial
from PermutationEnumerator import *

class Algebra:
    def __init__(
            self,
            dimension, # int
            multiplication, # cupy sparse matrix
            unit, # cupy dense vector
            star # cupy sparse matrix
    ):

        # dimension of algebra
        # we denote the basis vectors as e_1, e_2, ...., e_dimension
        self.dimension = dimension


        # dimension * i + j column is e_i e_j
        self.multiplication = multiplication

        # unit of algebra. Dense cupy array
        self.unit = unit



def symmetric_group(n):
    pe = PermutationEnumerator(n)
    dimension = ps.number_of_perms
