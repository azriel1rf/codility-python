def solution(N, P, Q):
    sieve = [0] * (N + 1)
    sieve[0] = sieve[1] = 3
    i = 2
    while i <= N:
        for j in range(2 * i, N + 1, i):
            sieve[j] += sieve[i] + 1
        i += 1

    prefix_sums = [0] * (N + 2)
    for i in range(1, N + 2):
        prefix_sums[i] = prefix_sums[i - 1] + (0 < sieve[i - 1] <= 2)

    result = []
    for p, q in zip(P, Q):
        result.append(prefix_sums[q + 1] - prefix_sums[p])
    return result
