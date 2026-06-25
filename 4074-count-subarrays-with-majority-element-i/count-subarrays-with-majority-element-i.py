class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                if nums[j] == target:
                    current_sum += 1
                else:
                    current_sum -= 1
                if current_sum > 0:
                    result += 1
        return result