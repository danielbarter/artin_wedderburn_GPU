from math import factorial

class PermutationEnumerator:
    def __init__(self, perm_length):
        """
        class for enumerating permutations.
        see https://gist.github.com/lukmdo/7049748
        compatible with itertools.permutations
        """
        self.perm_length = perm_length
        self.number_of_perms = factorial(perm_length)

    @staticmethod
    def int_from_code(code):
        """
        code: List[int]
        return: int
        """
        num = 0
        for i, v in enumerate(reversed(code), 1):
            num *= i
            num += v

        return num

    def code_from_int(self, num):
        """
        num: int
        return: List[int]
        """
        code = []
        for i in range(self.perm_length):
            num, j = divmod(num, self.perm_length - i)
            code.append(j)

        return code

    @staticmethod
    def perm_from_code(code):
        """
        base: List[int]
        code: List[int]
        return: List[int]
        """

        perm = list(range(len(code)))
        for i in range(len(code) - 1):
            j = code[i]
            perm[i], perm[i+j] = perm[i+j], perm[i]

        return perm

    @staticmethod
    def code_from_perm(perm):
        """
        base: List[int]
        perm: List[int]
        rtype: List[int]
        """
        p = list(range(len(perm)))
        n = len(perm)
        pos_map = {v: i for i, v in enumerate(p)}

        w = []
        for i in range(n):
            d = pos_map[perm[i]] - i
            w.append(d)

            if not d:
                continue
            t = pos_map[perm[i]]
            pos_map[p[i]], pos_map[p[t]] = pos_map[p[t]], pos_map[p[i]]
            p[i], p[t] = p[t], p[i]

        return w


    def perm_from_int(self, num):
        return self.perm_from_code(self.code_from_int(num))

    def int_from_perm(self,perm):
        return self.int_from_code(self.code_from_perm(perm))
