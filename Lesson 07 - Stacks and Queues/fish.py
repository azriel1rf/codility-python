def solution(A, B):
    survivors = 0
    stack = []
    for size, direction in zip(A, B):
        if direction == 1:
            stack.append(size)
        else:
            while stack and stack[-1] < size:
                stack.pop()
            if not stack:
                survivors += 1

    survivors += len(stack)
    return survivors
