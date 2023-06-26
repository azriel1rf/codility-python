def solution(S, P, Q):
    N = len(S)
    factors = {"A": 1, "C": 2, "G": 3, "T": 4}
    prefix_sum = {key: [0] * (N + 1) for key in "ACGT"}

    for i, char in enumerate(S):
        for key in "ACGT":
            prefix_sum[key][i + 1] = prefix_sum[key][i] + (key == char)

    result = []
    for p, q in zip(P, Q):
        for key in "ACGT":
            if prefix_sum[key][q + 1] - prefix_sum[key][p] > 0:
                result.append(factors[key])
                break
    return result
