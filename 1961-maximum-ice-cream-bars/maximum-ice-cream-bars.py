class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)
        for cost in costs:
            freq[cost] += 1

        max_count = 0
        for cost in range(1, max_cost + 1):
            if freq[cost] == 0:
                continue
            
            if coins < cost:
                break
            
            buy_count = min(freq[cost], coins//cost)

            max_count += buy_count
            coins -= cost * buy_count

        return max_count