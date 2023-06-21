def solution(N):
    min_perimeter = float("inf")
    i = 1
    while i * i <= N:
        if N % i == 0:
            perimeter = 2 * (i + N // i)
            min_perimeter = min(min_perimeter, perimeter)
        i += 1
    return min_perimeter
