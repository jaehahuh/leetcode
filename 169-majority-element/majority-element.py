class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = Counter(nums)
        for num in counts:
            if counts[num] > len(nums)/2:
                return num