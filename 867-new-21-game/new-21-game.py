class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= (k - 1) + maxPts:
            return 1

        # dp[i] = 점수 i에 도달할 확률 
        dp = [0.0] * (n + 1)
        dp[0] = 1.0

        result = 0.0
        window_sum = 1.0 # 현재 i에 기여할 수 있는 직전 진행 상태(<k) 확률 합

        for i in range(1, n+1):
            # i로 들어올 수 있는 모든 진행 상태들의 확률 합을 maxPts로 나눈 값
            dp[i] = window_sum/maxPts 

            if i < k:
                # i가 아직 진행 상태(<k)이면 다음 점수 계산에 기여하므로 window_sum에 포함
                window_sum += dp[i]
            else:
                # i가 종료 상태(≥k)이면 정답에 누적
                result += dp[i]
            
            left = i - maxPts
            if left >= 0 and left < k:
                window_sum -= dp[left]

        return result