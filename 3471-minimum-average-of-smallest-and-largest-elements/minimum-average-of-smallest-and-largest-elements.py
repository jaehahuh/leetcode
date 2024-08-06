class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()
        while nums:
            min_n = nums.pop(0)
            max_n = nums.pop()
            avg = (min_n + max_n)/2
            averages.append(avg)
            
        return min(averages) 