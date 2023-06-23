def solution(N):
    while N and N % 2 == 0:
        N >>= 1
    gap = max_gap = 0
    while N:
        if N % 2:
            max_gap = max(max_gap, gap)
            gap = 0
        else:
            gap += 1
        N >>= 1
    return max_gap
