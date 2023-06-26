def solution(A):
    N = len(A)
    min_avg = float("inf")
    min_pos = -1

    for i in range(N - 1):
        avg_2 = (A[i] + A[i + 1]) / 2
        if avg_2 < min_avg:
            min_avg = avg_2
            min_pos = i

        if i < N - 2:
            avg_3 = (A[i] + A[i + 1] + A[i + 2]) / 3
            if avg_3 < min_avg:
                min_avg = avg_3
                min_pos = i
    return min_pos
