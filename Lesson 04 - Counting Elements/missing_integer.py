def solution(A):
    A = set(A)
    smallest_positive = 1
    while smallest_positive in A:
        smallest_positive += 1
    return smallest_positive
