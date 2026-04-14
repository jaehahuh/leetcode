class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        factory_positions = []
        for pos, limit in factory:
            factory_positions.extend([pos] * limit)
        
        n, m = len(robot), len(factory_positions)

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 0
        
        for i in range(1, m + 1): 
            for j in range(1, n + 1): 
                dp[i][j] = dp[i-1][j]
                
                res = dp[i-1][j-1] + abs(robot[j-1] - factory_positions[i-1])
                dp[i][j] = min(dp[i][j], res)
                
        return dp[m][n]