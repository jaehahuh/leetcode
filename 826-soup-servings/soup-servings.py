class Solution:
    def soupServings(self, n: int) -> float:
        # Secure approximation optimization for large n
        if n >= 4800:
            return 1.0

        m = (n + 24) // 25 # Ex) n = 0 ~ 25, m = 0 ; n = 26 ~ 50, m = 1 ..
        dp = [[0,0]*(m+1) for _ in range(m + 1)]

        # Base case
        dp[0][0] = 0.5
        for b in range(1, m + 1):
            dp[0][b] = 1.0 # a <= 0, b > 0
        for a in range(1, m + 1):
            dp[a][0] = 0.0 # a > 0, b <= 0
      
        def get(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return dp[a][b]
        
        for a in range(1, m + 1):
            for b in range(1, m + 1):
                dp[a][b] = 0.25 * (get(a-4, b) + get(a-3, b-1) + get(a-2, b-2) + get(a-1, b-3))

        return dp[m][m]