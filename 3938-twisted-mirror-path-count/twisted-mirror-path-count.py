class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[0, 0] for _ in range(n + 1)]
        dp[1] = [1, 1] 
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # 위쪽에서 내려온 경로 -> 오른쪽으로 꺾임, 왼쪽에서 온 경로 -> 아래쪽으로 꺾임
                    dp[c + 1] = [dp[c + 1][1], dp[c][0]]
                else:
                    # 위쪽과 왼쪽에서 오는 경로들의 합
                    total = (dp[c + 1][1] + dp[c][0]) % MOD
                    dp[c + 1] = [total, total]
                    
        return dp[n][0]