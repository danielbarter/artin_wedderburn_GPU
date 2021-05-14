from PermutationEnumerator import *
from itertools import permutations
from ArtinWedderburn import *

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
            print(bcolors.FAIL, "failed: int_to_perm_to_int", bcolors.ENDC)
            return

    print(bcolors.OKGREEN, "passed: int_to_perm_to_int", bcolors.ENDC)

def perm_to_int_to_perm():
    pe = PermutationEnumerator(4)
    for p in permutations(list(range(pe.perm_length))):
        pl = list(p)
        if pe.perm_from_int(pe.int_from_perm(pl)) != pl:
            print(bcolors.FAIL, "failed: perm_to_int_to_perm", bcolors.ENDC)
            return

    print(bcolors.OKGREEN, "passed: perm_to_int_to_perm", bcolors.ENDC)


def total_defect_test(algebra, name, defect_threshold=1.0e-5):
    print("\n\n")
    aw = ArtinWedderburn(algebra, logging=True)
    if aw.total_defect < defect_threshold:
        print(bcolors.OKGREEN, "passed: total_defect_test", name, bcolors.ENDC)
    else:
        print(bcolors.FAIL, "failed: total_defect_test", name, bcolors.ENDC)

    print("\n\n")


int_to_perm_to_int()
perm_to_int_to_perm()
a2 = symmetric_group(2)
a3 = symmetric_group(3)
a4 = symmetric_group(4)
total_defect_test(a2, "S2")
total_defect_test(a3, "S3")
total_defect_test(a4, "S4")
