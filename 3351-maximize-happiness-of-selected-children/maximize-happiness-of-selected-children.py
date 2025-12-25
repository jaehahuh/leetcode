class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        max_happiness = 0
        top_k_happiness = heapq.nlargest(k, happiness)
        decrement = 0
        for happiness in top_k_happiness:
            curr_value = happiness - decrement
            if curr_value > 0:
                max_happiness += curr_value
            decrement += 1
    
        return max_happiness