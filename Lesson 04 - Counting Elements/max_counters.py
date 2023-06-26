def solution(N, A):
    counters = [0] * N
    max_counter = 0
    last_update = 0

    for command in A:
        if command == N + 1:
            last_update = max_counter
        else:
            command -= 1
            counters[command] = max(counters[command], last_update)
            counters[command] += 1
            max_counter = max(max_counter, counters[command])

    for i in range(N):
        counters[i] = max(last_update, counters[i])

    return counters
