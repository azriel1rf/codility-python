def solution(A, B):
    max_a = max(A)
    max_b = max(B)
    p = 2**max_b

    fibs = [1, 1] + [0] * (max_a - 1)
    for i in range(2, max_a + 1):
        fibs[i] = (fibs[i - 1] + fibs[i - 2]) % p

    result = []
    for a, b in zip(A, B):
        result.append(fibs[a] % (2**b))
    return result
