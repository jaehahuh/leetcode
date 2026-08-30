class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        front = min(min_idx, max_idx)
        back = max(min_idx, max_idx)

        return min(back + 1, n - front, (front + 1) + (n - back))