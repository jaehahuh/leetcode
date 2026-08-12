class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        count_dict = defaultdict(int)
        longest_sub = 0
        n = len(nums)
        for right in range(n):
            count_dict[nums[right]] += 1
            while count_dict[nums[right]] > k:
                count_dict[nums[left]] -= 1
                left += 1
            longest_sub = max(longest_sub, right - left + 1)

        return longest_sub