import cupy as cp
import cupyx.scipy.sparse as sparse
from cupy.linalg import eigh
from math import factorial
from PermutationEnumerator import *

def fuzzy_filter(array, threshold):
    result = []
    for x in array:
        already_seen = False
        for v in result:
            if abs(x-v) < threshold:
                already_seen = True
                break

        if not already_seen:
            result.append(x)

    return result



class ArtinWedderburn:
    def eigenvalues_of_pivot(self):
        left_multiplication = self.algebra.left_multiplication_matrix(
            self.pivot)
        all_eigenvalues = eigh(left_multiplication)[0].tolist()
        return fuzzy_filter(all_eigenvalues, self.threshold)

    def compute_indecomposable_idempotents(self):
        eigenvalues = eigenvalues_of_pivot()
        number_of_eigenvalues = len(eigenvalues)
        for i in range(number_of_eigenvalues):
            accumulator = self.algebra.unit
            for j in range(number_of_eigenvalues):
                pass


    def __init__(self, algebra, threshold = 1.0e-5, logging = False):
        self.algebra = algebra
        self.threshold = threshold
        self.logging = logging


        self.pivot = algebra.random_positive_vector()


class Algebra:
    def associative_defect(self):
        x = self.random_vector()
        y = self.random_vector()
        z = self.random_vector()
        l = self.multiply(self.multiply(x,y), z)
        r = self.multiply(x, self.multiply(y,z))
        return cp.sum(cp.abs(l - r)).tolist()

    def left_identity_defect(self):
        lm = self.left_multiplication_matrix(self.unit)
        return cp.sum(cp.abs(lm - cp.identity(self.dimension))).tolist()

    def algebra_defect(self):
        return sum([self.associative_defect(),
                    self.associative_defect(),
                    self.associative_defect(),
                    self.left_identity_defect()])


    def random_vector(self):
        d = self.dimension
        return (cp.random.rand(d) - 0.5 ) + 1j * (cp.random.rand(d) - 0.5 )

    def random_positive_vector(self):
        v = self.random_vector()
        return self.multiply(
            v,
            self.star(v))

    def multiply(self, x, y):
        return self.multiplication * cp.kron(x,y)

    def star(self, x):
        return self.star_mat * (x.conj())


    def mult_helper(self,v, ms):
        # ms is a list of sparse matrices
        d = self.dimension
        accumulator = cp.zeros((d,d), dtype=complex)

        for (c, m) in zip(v, ms):
            accumulator += c * m.todense()

        return accumulator

    def left_multiplication_matrix(self,v):
        return self.mult_helper(v, self.left_multiplication_matrices)



    def __init__(
            self,
            dimension, # int
            left_multiplication_matrices, # list of cupy sparse matrices
            unit, # cupy dense vector
            star # cupy sparse matrix
    ):

        # dimension of algebra
        # we denote the basis vectors as e_1, e_2, ...., e_dimension
        self.dimension = dimension

        # list of matrices
        # jth column of ith matrix is e_i e_j
        self.left_multiplication_matrices = left_multiplication_matrices

        # dimension * i + j column is e_i e_j
        # sparse cupy matrix
        self.multiplication = sparse.hstack(left_multiplication_matrices)

        # unit of algebra. Dense cupy array
        self.unit = unit

        # jth column is e_j*
        # sparse cupy matrix
        self.star_mat = star



def symmetric_group(n):
    pe = PermutationEnumerator(n)
    dimension = pe.number_of_perms
    left_multiplication_matrices = []

    for i in range(dimension):

        data_mult = cp.ndarray((dimension), dtype=complex)
        col_mult = cp.ndarray((dimension), dtype=int)
        row_mult = cp.ndarray((dimension), dtype=int)

        for j in range(dimension):
            p1 = pe.perm_from_int(i)
            p2 = pe.perm_from_int(j)
            p3 = multiply_permutations(p1, p2)
            k = pe.int_from_perm(p3)
            col_index = j
            data_mult[col_index] = 1.0
            col_mult[col_index] = col_index
            row_mult[col_index] = k

        left_multiplication = sparse.coo_matrix(
            (data_mult, (row_mult, col_mult)),
            shape=(dimension, dimension),
            dtype=complex)

        left_multiplication_matrices.append(left_multiplication)

    unit = cp.ndarray((dimension), dtype=complex)
    unit[pe.int_from_perm(pe.base)] = 1.0

    data_star = cp.ndarray((dimension), dtype=complex)
    col_star = cp.ndarray((dimension), dtype=int)
    row_star = cp.ndarray((dimension), dtype=int)

    for j in range(dimension):
        p = pe.perm_from_int(j)
        p_inv = inverse_permutation(p)
        i = pe.int_from_perm(p_inv)
        data_star[j] = 1.0
        col_star[j] = j
        row_star[j] = i

    star = sparse.coo_matrix(
        (data_star, (row_star, col_star)),
        shape = (dimension, dimension),
        dtype=complex)

    return Algebra(
        dimension,
        left_multiplication_matrices,
        unit,
        star)



