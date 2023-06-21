from collections import Counter


def solution(A):
    max_a = max(A)
    count = Counter(A)
    sieve = [len(A)] * (max_a + 1)
    for k, v in count.items():
        for i in range(k, max_a + 1, k):
            sieve[i] -= v

    return [sieve[a] for a in A]
