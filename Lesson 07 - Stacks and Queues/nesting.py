def solution(S):
    opens = 0
    for char in S:
        if char == ")":
            if opens > 0:
                opens -= 1
            else:
                return 0
        else:
            opens += 1
    return int(opens == 0)
