def solution(A):
    N = len(A)
    return int(set(A) == set(range(1, N + 1)))
