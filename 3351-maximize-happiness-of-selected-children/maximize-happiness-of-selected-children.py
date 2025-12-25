class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        max_happiness = 0
        happiness.sort(reverse=True)
        decrement = 0
        for i in range(k):
            curr_value = happiness[i] - decrement
            if curr_value > 0:
                max_happiness += happiness[i] - decrement
            else:
                max_happiness += 0
            decrement += 1
    
        return max_happiness   