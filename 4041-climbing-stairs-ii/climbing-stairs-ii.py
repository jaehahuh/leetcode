class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp0, dp1, dp2 = float('inf'), float('inf'), 0

        for i in range(1, n + 1):
            cost_i = costs[i - 1]
        
            # 1-step (k=1, k^2=1), 2-step (k=2, k^2=4), 3-step (k=3, k^2=9)
            curr = cost_i + min(dp2 + 1, dp1 + 4, dp0 + 9)
            
            # 슬라이딩 윈도우 갱신
            dp0, dp1, dp2 = dp1, dp2, curr

        return dp2