class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        h = k // 2

        sp_values = [s * p for s, p in zip(strategy, prices)]
        base_profit = sum(sp_values)
        
        max_profit = base_profit

        current_original_window_profit = sum(sp_values[0:k])
        current_modified_window_profit = sum(prices[h:k])

        current_delta_profit = current_modified_window_profit - current_original_window_profit
        max_profit = max(max_profit, base_profit + current_delta_profit)
        
        for i in range(1, n - k + 1):
            current_original_window_profit = (current_original_window_profit - sp_values[i-1]) + sp_values[i+k-1]
            current_modified_window_profit = (current_modified_window_profit - prices[i + h - 1]) + prices[i + k - 1]

            current_delta_profit = current_modified_window_profit - current_original_window_profit
            max_profit = max(max_profit, base_profit + current_delta_profit)
            
        return max_profit