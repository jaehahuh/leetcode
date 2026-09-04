class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        smallest = [0] * n
        smallest[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            smallest[i] = min(smallest[i + 1], nums[i])

        largest = float('-inf')
        for i in range(n):
            largest = max(largest, nums[i])
            score = largest - smallest[i]
            if score <= k:
                return i 
        
        return -1