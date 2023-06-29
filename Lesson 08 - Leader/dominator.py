from collections import Counter


def solution(A):
    if not A:
        return -1

    counter = Counter(A)
    dominator, count = counter.most_common(1)[0]
    if count > len(A) / 2:
        return A.index(dominator)
    else:
        return -1
