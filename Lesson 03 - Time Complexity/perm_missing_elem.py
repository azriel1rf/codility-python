def solution(A):
    N = len(A)
    return (set(range(1, N + 2)) - set(A)).pop()
