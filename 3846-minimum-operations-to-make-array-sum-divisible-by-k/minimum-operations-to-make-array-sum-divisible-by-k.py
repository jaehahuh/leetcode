class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        remainder = total % k
        op = remainder
        return op