class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        orignal_profit = 0
        for i in range(n):
            orignal_profit += prices[i] * strategy[i]
        
        max_profit = orignal_profit
        
        #prefix_sum
        buy_delta_values = [-s * p for s, p in zip(strategy, prices)]
        sell_delta_values = [(1 - s) * p for s, p in zip(strategy, prices)]

        prefix_buy_delta = [0] * (n + 1)
        for i in range(n):
            prefix_buy_delta[i+1] = prefix_buy_delta[i] + buy_delta_values[i]
        
        prefix_sell_delta = [0] * (n + 1)
        for i in range(n):
            prefix_sell_delta[i+1] = prefix_sell_delta[i] + sell_delta_values[i]

        
        for i in range(n - k + 1):
            hold_sum = prefix_buy_delta[i + (k//2)] - prefix_buy_delta[i]
            sell_sum = prefix_sell_delta[i + k] - prefix_sell_delta[i + (k//2)]
            current_delta_profit = hold_sum + sell_sum
            max_profit = max(max_profit, orignal_profit + current_delta_profit)
            
        return max_profit