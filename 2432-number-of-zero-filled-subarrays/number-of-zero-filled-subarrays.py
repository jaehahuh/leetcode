class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        num_subarray = 0
        curr_zeros = 0
        for n in nums:
            if n == 0:
                curr_zeros += 1
                num_subarray += curr_zeros
            else:
                curr_zeros = 0
        return num_subarray