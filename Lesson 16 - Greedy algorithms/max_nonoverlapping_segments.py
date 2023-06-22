def solution(A, B):
    count = 0
    last_b = -1

    for a, b in zip(A, B):
        if last_b < a:
            last_b = b
            count += 1

    return count
