def solution(X, A):
    fallen_leaves = set()
    for i, a in enumerate(A):
        fallen_leaves.add(a)
        if len(fallen_leaves) == X:
            return i
    return -1
