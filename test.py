from PermutationEnumerator import *
from itertools import permutations

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def int_to_perm_to_int():
    pe = PermutationEnumerator(4)
    for i in range(pe.number_of_perms):
        if pe.int_from_perm(pe.perm_from_int(i)) != i:
            print(bcolors.FAIL + "failed: int_to_perm_to_int" + bcolors.ENDC)
            return

    print(bcolors.OKGREEN + "passed: int_to_perm_to_int" + bcolors.ENDC)

def perm_to_int_to_perm():
    pe = PermutationEnumerator(4)
    for p in permutations(list(range(pe.perm_length))):
        pl = list(p)
        if pe.perm_from_int(pe.int_from_perm(pl)) != pl:
            print(bcolors.FAIL + "failed: perm_to_int_to_perm" + bcolors.ENDC)
            return

    print(bcolors.OKGREEN + "passed: perm_to_int_to_perm" + bcolors.ENDC)


int_to_perm_to_int()
perm_to_int_to_perm()
