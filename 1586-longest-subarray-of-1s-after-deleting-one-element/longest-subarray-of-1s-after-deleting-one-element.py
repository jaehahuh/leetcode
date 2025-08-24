class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        count_zero, count_one = 0, 0
        longest_one = 0
        left = 0
        for right in range(n):
            if nums[right] == 1:
                count_one += 1
                longest_one = max(longest_one, count_one)
            else:
                count_zero += 1
            while count_zero >= 2:
                if nums[left] == 1:
                    count_one -= 1
                    left += 1
                else:
                    count_zero -= 1
                    left += 1

        return longest_one if longest_one != n else longest_one - 1