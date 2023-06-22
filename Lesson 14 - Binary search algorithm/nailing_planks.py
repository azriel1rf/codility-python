# Meguru-style binary search
def is_valid(nail_count, A, B, C):
    MAX_POSITION = 2 * len(C)
    prefix_sums = [0] * (MAX_POSITION + 1)

    for c in C[:nail_count]:
        prefix_sums[c] = 1

    for i in range(1, len(prefix_sums)):
        prefix_sums[i] += prefix_sums[i - 1]

    for a, b in zip(A, B):
        if prefix_sums[a - 1] >= prefix_sums[b]:
            return False
    return True


def solution(A, B, C):
    if not is_valid(len(C), A, B, C):
        return -1
    invalid = 0
    valid = len(C)

    while abs(invalid - valid) > 1:
        mid = (valid + invalid) // 2
        if is_valid(mid, A, B, C):
            valid = mid
        else:
            invalid = mid

    return valid
