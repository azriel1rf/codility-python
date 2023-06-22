def solution(K, A):
    count = 0
    length = 0
    for rope in A:
        length += rope
        if length >= K:
            count += 1
            length = 0
    return count
