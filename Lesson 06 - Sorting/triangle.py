def solution(A):
    N = len(A)
    A.sort(reverse=True)
    for i in range(N - 2):
        if A[i] < A[i + 1] + A[i + 2]:
            return 1
    return 0
