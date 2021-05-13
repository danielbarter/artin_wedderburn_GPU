def int_from_code(code):
    """
    https://gist.github.com/lukmdo/7049748
    code: List[int]
    return: int
    """
    num = 0
    for i, v in enumerate(reversed(code), 1):
        num *= i
        num += v

    return num

def code_from_int(size, num):
    """
    https://gist.github.com/lukmdo/7049748
    size: int
    num: int
    return: List[int]
    """
    code = []
    for i in range(size):
        num, j = divmod(num, size - i)
        code.append(j)

    return code

def perm_from_code(base, code):
    """
    https://gist.github.com/lukmdo/7049748
    base: List[int]
    code: List[int]
    return: List[int]
    """

    perm = base.copy()
    for i in range(len(base) - 1):
        j = code[i]
        perm[i], perm[i+j] = perm[i+j], perm[i]

    return perm

def code_from_perm(base, perm):
    """
    https://gist.github.com/lukmdo/7049748
    base: List[int]
    perm: List[int]
    rtype: List[int]
    """
    p = base.copy()
    n = len(base)
    pos_map = {v: i for i, v in enumerate(base)}

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
