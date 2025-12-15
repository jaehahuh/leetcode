class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        dp[0] = 1

        smooth_periods = dp[0]
        for i in range(1, n):
            if prices[i-1] - prices[i] == 1:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1 # prices[i] starts a new smooth descent period
            
            smooth_periods += dp[i]
        
        return smooth_periods