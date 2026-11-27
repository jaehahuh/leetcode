class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for _, price in items)

        # free_gain[i]: 아이템 i를 1개 이상 구매했을 때 얻는 공짜 아이템 수
        free_gain = [0] * n
        for i in range(n):
            fi, _ = items[i]
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1
            free_gain[i] = cnt

        # dp[b]: 예산 b를 써서 '최소 1개 이상 구매할 아이템 집합'을 골랐을 때의
        # (선택한 아이템 수 + 해당 아이템들로 얻는 공짜 아이템 수)의 최댓값
        NEG_INF = -10**9
        dp = [NEG_INF] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            _, price = items[i]
            gain_if_picked = 1 + free_gain[i]  # 구매 1개 + 공짜 이득
            if price <= budget:
                # 0-1 선택처럼 뒤에서부터 순회해 한 아이템당 최대 한 번만 '1개 이상 구매'로 반영
                for b in range(budget, price - 1, -1):
                    if dp[b - price] != NEG_INF:
                        dp[b] = max(dp[b], dp[b - price] + gain_if_picked)

        # 남은 예산을 모두 가장 싼 아이템(min_price) 구매에 사용
        ans = 0
        for b in range(budget + 1):
            if dp[b] != NEG_INF:
                extra_bought = (budget - b) // min_price
                ans = max(ans, dp[b] + extra_bought)

        return ans