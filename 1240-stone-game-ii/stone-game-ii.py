class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n)]
    
        suffix_sum = 0
        
        for i in range(n - 1, -1, -1):
            suffix_sum += piles[i]
            
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix_sum
                else:
                    for x in range(1, 2 * m + 1):
                        dp[i][m] = max(
                            dp[i][m], 
                            suffix_sum - dp[i + x][max(m, x)]
                        )
                        
        return dp[0][1]