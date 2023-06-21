# Kadane's algorithm
def solution(A):
    max_ending_here = max_ending_so_far = A[0]
    for num in A[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_ending_so_far = max(max_ending_so_far, max_ending_here)
    return max_ending_so_far
