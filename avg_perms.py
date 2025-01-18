from itertools import permutations
def permutation_average(n):
    digs = list(str(n))
    perms = list(permutations(digs))
    res = [int(''.join(p)) for p in perms]
    summed = sum(res)
    avg = summed / len(res)
    return round(avg)