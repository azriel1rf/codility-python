from collections import Counter


def solution(A):
    N = len(A)
    counter = Counter(A)
    leader = counter.most_common(1)[0][0]
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + (A[i] == leader)

    result = 0
    for i in range(N - 1):
        if (
            prefix_sum[i + 1] > (i + 1) / 2
            and prefix_sum[N] - prefix_sum[i + 1] > (N - i - 1) / 2
        ):
            result += 1
    return result
