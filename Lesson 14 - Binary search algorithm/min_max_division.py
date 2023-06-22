# Meguru-style binary search
def is_valid(n, K, A):
    # Check if A can be divided into K blocks with each block sum <= n
    cum = 0
    count = 0
    for a in A:
        if cum + a > n:
            count += 1
            cum = a
        else:
            cum += a
    if cum > 0:
        count += 1
    return count <= K


def solution(K, M, A):
    valid = sum(A)
    invalid = max(A) - 1
    while abs(valid - invalid) > 1:
        mid = (valid + invalid) // 2
        if is_valid(mid, K, A):
            valid = mid
        else:
            invalid = mid
    return valid
