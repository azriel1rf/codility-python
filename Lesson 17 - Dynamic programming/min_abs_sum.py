from collections import Counter


def solution(A):
    if not A:
        return 0

    A = [abs(a) for a in A]
    total_sum = sum(A)
    max_element = max(A)
    count = Counter(A)

    dp = [-1] * (total_sum + 1)
    dp[0] = 0
    for i in range(1, max_element + 1):
        if i in count:
            for j in range(total_sum):
                if dp[j] >= 0:
                    dp[j] = count[i]
                elif j >= i and dp[j - i] > 0:
                    dp[j] = dp[j - i] - 1

    result = total_sum
    for i in range(total_sum // 2 + 1):
        if dp[i] >= 0:
            result = min(result, total_sum - 2 * i)

    return result
