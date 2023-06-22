def solution(M, A):
    N = len(A)
    front = back = 0
    nums = set()
    result = 0
    while front < N:
        while front < N and A[front] not in nums:
            nums.add(A[front])
            front += 1
        while nums and (front == N or A[front] in nums):
            result += front - back
            if result > 1_000_000_000:
                return 1_000_000_000
            nums.remove(A[back])
            back += 1
    return result
