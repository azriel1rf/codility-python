def solution(A):
    points = []
    for i, a in enumerate(A):
        points.append((i - a, -1))  # start point
        points.append((i + a, 1))  # end point
    points.sort()

    intersections = 0
    open_discs = 0
    for _, is_start in points:
        if is_start == -1:
            intersections += open_discs
            open_discs += 1
        else:
            open_discs -= 1
        if intersections > 10000000:
            return -1
    return intersections
