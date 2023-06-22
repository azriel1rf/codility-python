import math


def has_same_primes(target, source):
    while target != 1:
        gcd = math.gcd(target, source)
        if gcd == 1:
            return False
        target //= gcd
    return True


def solution(A, B):
    result = 0
    for a, b in zip(A, B):
        gcd = math.gcd(a, b)
        if has_same_primes(a // gcd, gcd) and has_same_primes(b // gcd, gcd):
            result += 1
    return result
