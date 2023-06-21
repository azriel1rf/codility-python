def solution(heights):
    N = len(heights)
    if N < 3:
        return 0

    peaks = [False] * N
    for i in range(1, N - 1):
        if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
            peaks[i] = True

    next_peak = [0] * N
    next_peak[-1] = -1
    for i in range(N - 1)[::-1]:
        if peaks[i]:
            next_peak[i] = i
        else:
            next_peak[i] = next_peak[i + 1]

    max_flags = 0
    distance = 1
    while (distance - 1) * distance <= N:
        num_flags = 0
        pos = 0
        while pos < N and num_flags < distance:
            pos = next_peak[pos]
            if pos == -1:
                break
            pos += distance
            num_flags += 1
        max_flags = max(max_flags, num_flags)
        distance += 1

    return max_flags
