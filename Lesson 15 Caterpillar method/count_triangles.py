def solution(A):
    A.sort()
    N = len(A)
    result = 0
    for left in range(N):
        right = left + 2
        for mid in range(left + 1, N):
            while right < N and A[left] + A[mid] > A[right]:
                right += 1
            result += max(0, right - mid - 1)
    return result
