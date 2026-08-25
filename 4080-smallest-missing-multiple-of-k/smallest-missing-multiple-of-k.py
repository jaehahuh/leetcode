class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        smallest_missing = k

        while smallest_missing in nums_set:
            smallest_missing += k
        
        return smallest_missing