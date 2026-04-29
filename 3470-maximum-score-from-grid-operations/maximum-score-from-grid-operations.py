class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        if n == 1: return 0

        dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n)]

        prev_max = [[0] * (n + 1) for _ in range(n + 1)]
        prev_suffix_max = [[0] * (n + 1) for _ in range(n + 1)]
        
        col_sum = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            for r in range(1, n + 1):
                col_sum[c][r] = col_sum[c][r - 1] + grid[r - 1][c]
        
        for i in range(1, n): # 1번째 열부터 마지막 열까지 진행
            for curr_h in range(n + 1): # 현재 열 i의 높이 결정
                for prev_h in range(n + 1): # 이전 열 i-1의 높이 결정
                    if curr_h <= prev_h:
                        # 현재 열(i)의 흰 칸 중, 이전 열(i-1)의 검은 칸과 닿는 구간의 점수
                        extra_score = col_sum[i][prev_h] - col_sum[i][curr_h]
                        dp[i][curr_h][prev_h] = max(
                            dp[i][curr_h][prev_h],
                            prev_suffix_max[prev_h][0] + extra_score
                        )
                    else: # curr_h > prev_h
                        # 이전 열(i-1)의 흰 칸 중, 현재 열(i)의 검은 칸과 닿는 구간의 점수
                        extra_score = col_sum[i - 1][curr_h] - col_sum[i - 1][prev_h]
                        dp[i][curr_h][prev_h] = max(
                            dp[i][curr_h][prev_h],
                            prev_suffix_max[prev_h][curr_h], # 이미 보정된 최댓값 참조
                            prev_max[prev_h][curr_h] + extra_score # 이전 열이 얻을 추가 점수 합산
                        )
            
            for curr_h in range(n + 1):
                prev_max[curr_h][0] = dp[i][curr_h][0]
                for prev_h in range(1, n + 1):
                    # 중복 계산 방지용 패널티: 현재 열의 점수가 이미 포함되었다면 이를 빼고 비교해야 합니다.
                    penalty = (col_sum[i][prev_h] - col_sum[i][curr_h] if prev_h > curr_h else 0)
                    prev_max[curr_h][prev_h] = max(
                        prev_max[curr_h][prev_h - 1],
                        dp[i][curr_h][prev_h] - penalty
                    )
                prev_suffix_max[curr_h][n] = dp[i][curr_h][n]
                for prev_h in range(n - 1, -1, -1):
                    prev_suffix_max[curr_h][prev_h] = max(
                        prev_suffix_max[curr_h][prev_h + 1],
                        dp[i][curr_h][prev_h]
                    )
        ans = 0
        for k in range(n + 1):
            # 마지막 열을 다 칠하거나(n), 하나도 안 칠했을 때(0)의 모든 경로 중 최댓값
            ans = max(ans, dp[n - 1][n][k], dp[n - 1][0][k])
        return ans