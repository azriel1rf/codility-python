from collections import deque


def solution(A, K):
    if not A:
        return A
    A = deque(A)
    for _ in range(K):
        A.appendleft(A.pop())
    return list(A)
