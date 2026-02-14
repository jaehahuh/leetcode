class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * (k + 1) for k in range(query_row + 2)]   # Each row k has k+1 glasses
        dp[0][0] = poured

        for i in range(query_row + 1):
            for j in range(i + 1):
                if dp[i][j] > 1: # Check if the current glass overflows (has more than 1 cup)
                    excess = dp[i][j] - 1
                    dp[i][j] = 1 # Keep the current glass filled to its max capacity (1 cup)
                    # Distribute the excess champagne equally to the two glasses below.
                    dp[i+1][j] += excess/2
                    dp[i+1][j+1] += excess/2

        return min(1, dp[query_row][query_glass])