def solution(S):
    pars = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    stack = []
    for char in S:
        if char in pars:
            if stack and stack[-1] == pars[char]:
                stack.pop()
            else:
                return 0
        else:
            stack.append(char)
    return int(not stack)
