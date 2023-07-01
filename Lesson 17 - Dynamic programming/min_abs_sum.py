from collections import Counter


def solution(A):
    A = [abs(a) for a in A]
    value_counts = Counter(A)
    total_sum = sum(A)

    reachable_sums = [0] * (total_sum // 2 + 1)
    reachable_sums[0] = 1
    counts_for_sums = [0] * (total_sum // 2 + 1)

    for value, count in value_counts.items():
        if value == 0:
            continue
        for i in range(len(reachable_sums)):
            if reachable_sums[i]:
                counts_for_sums[i] = count
        for i in range(value, len(reachable_sums)):
            if reachable_sums[i]:
                continue
            if reachable_sums[i - value] and counts_for_sums[i - value] > 0:
                reachable_sums[i] = 1
                counts_for_sums[i] = counts_for_sums[i - value] - 1

    min_val = float("inf")
    for i in range(len(reachable_sums)):
        if reachable_sums[i]:
            positive_sum = i
            negative_sum = -(total_sum - i)
            val = abs(positive_sum + negative_sum)
            min_val = min(min_val, val)

    return min_val
