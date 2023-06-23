from itertools import accumulate


def solution(A):
    cumsum = list(accumulate(A))
    total = cumsum[-1]
    min_diff = min(abs(total - 2 * s) for s in cumsum[:-1])
    return min_diff
