def solution(H):
    stack = []
    count = 0
    for h in H:
        while stack and stack[-1] > h:
            stack.pop()
        if not stack or stack[-1] != h:
            stack.append(h)
            count += 1
    return count
