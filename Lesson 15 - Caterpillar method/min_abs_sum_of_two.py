def solution(A):
    A.sort()
    back = 0
    front = len(A) - 1
    min_sum = float("inf")

    while back <= front:
        current_sum = A[back] + A[front]
        min_sum = min(min_sum, abs(current_sum))

        if current_sum <= 0:
            back += 1
        else:
            front -= 1

    return min_sum
