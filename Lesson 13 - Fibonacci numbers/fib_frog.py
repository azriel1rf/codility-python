from collections import deque


def solution(A):
    A.append(1)
    N = len(A)
    fibs = [1, 1]
    while True:
        next_fib = fibs[-1] + fibs[-2]
        if next_fib > N:
            break
        fibs.append(next_fib)
    # remove redundant 1 and reverse
    fibs = fibs[1::][::-1]

    steps = {-1: 0}
    queue = deque([-1])
    while queue and N - 1 not in steps:
        pos = queue.popleft()
        for fib in fibs:
            next_pos = pos + fib
            if next_pos < N and A[next_pos] and next_pos not in steps:
                steps[next_pos] = steps[pos] + 1
                queue.append(next_pos)
            if next_pos == N - 1:
                break

    return steps.get(N - 1, -1)
