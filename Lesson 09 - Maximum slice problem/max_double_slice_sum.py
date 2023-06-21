def solution(A):
    n = len(A)
    left_max_sum = [0] * n
    right_max_sum = [0] * n

    for i in range(1, n - 1):
        left_max_sum[i] = max(0, left_max_sum[i - 1] + A[i])

    for i in range(1, n - 1)[::-1]:
        right_max_sum[i] = max(0, right_max_sum[i + 1] + A[i])

    result = 0

    for i in range(1, n - 1):
        result = max(result, left_max_sum[i - 1] + right_max_sum[i + 1])

    return result
