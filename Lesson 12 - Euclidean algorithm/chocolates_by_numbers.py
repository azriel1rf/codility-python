# Euclidean algorithm
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def solution(N, M):
    return lcm(N, M) // M
