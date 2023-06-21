def solution(N):
    num_factors = 0
    i = 1
    while i * i < N:
        if N % i == 0:
            num_factors += 2
        i += 1
    if i * i == N:
        num_factors += 1
    return num_factors
