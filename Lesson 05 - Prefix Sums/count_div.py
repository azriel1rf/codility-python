def solution(A, B, K):
    # ceil(A / K) * K
    A = (A + K - 1) // K * K
    # floor(B / K) * K
    B = B // K * K
    return (B - A) // K + 1
