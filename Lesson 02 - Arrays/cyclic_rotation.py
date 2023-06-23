from collections import deque


def solution(A, K):
    if not A:
        return A
    A = deque(A)
    A.rotate(K)
    return list(A)
