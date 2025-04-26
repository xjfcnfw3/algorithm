class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        dp = [[1] * 34] + [[1] + [0] * 34 for _ in range(33)]
        if rowIndex == 0:
            return [1]
        for i in range(1, 34):
            for j in range(1, 34):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return [dp[rowIndex - i][i] for i in range(rowIndex + 1)]