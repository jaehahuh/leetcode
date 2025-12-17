class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        hold = [float('-inf')] * (k + 1)
        short = [float('-inf')] * (k + 1)
        free = [0] * (k + 1)

        for price in prices:
            for t in range(k, 0, -1):
                free[t] = max(free[t], hold[t] + price, short[t] - price)
                hold[t] = max(hold[t], free[t-1] - price)
                short[t] = max(short[t], free[t-1] + price)
        return max(free)