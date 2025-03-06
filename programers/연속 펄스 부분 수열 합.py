def solution(sequence):
    dp = [[0] * 2 for _ in range(len(sequence))]
    dp[0][0], dp[0][1] = sequence[0], -sequence[0]
    answer = max(dp[0])
    for i in range(1, len(sequence)):
        dp[i][0] = max(dp[i - 1][1] + sequence[i], sequence[i])
        dp[i][1] = max(dp[i - 1][0] - sequence[i], -sequence[i])
        answer = max(answer, dp[i][0], dp[i][1])
    return answer