def solution(A):
    N = len(A)

    peaks = set()
    for i in range(1, N - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.add(i)

    prefix_sums = [0] * (N + 1)
    for i in range(N):
        prefix_sums[i + 1] = prefix_sums[i] + (i in peaks)

    factors = []
    i = 1
    while i * i <= N:
        if N % i == 0:
            factors.append(i)
            if N // i != i:
                factors.append(N // i)
        i += 1
    factors.sort()

    for num_blocks in reversed(factors):
        block_size = N // num_blocks
        if all(
            prefix_sums[i] < prefix_sums[i + block_size]
            for i in range(0, N + 1 - block_size, block_size)
        ):
            return num_blocks
    return 0
