def find_peaks(heights):
    num_peaks = len(heights)
    peaks = [False] * num_peaks

    for i in range(1, num_peaks - 1):
        if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
            peaks[i] = True

    return peaks


def find_next_peak(heights, peaks):
    next_peak = [0] * len(heights)
    next_peak[-1] = -1

    for i in range(len(heights) - 2, -1, -1):
        if peaks[i]:
            next_peak[i] = i
        else:
            next_peak[i] = next_peak[i + 1]

    return next_peak


def solution(heights):
    if len(heights) < 3:
        return 0

    peaks = find_peaks(heights)
    next_peak = find_next_peak(heights, peaks)

    max_flags = 0
    for distance in range(1, len(heights)):
        if distance * (distance - 1) > len(heights):
            break

        num_flags = 0
        pos = 0
        while pos < len(heights) and num_flags < distance:
            pos = next_peak[pos]
            if pos == -1:
                break
            pos += distance
            num_flags += 1

        max_flags = max(max_flags, num_flags)

    return max_flags
