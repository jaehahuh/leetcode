class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    value_of_triplet = (nums[i] - nums[j]) * nums[k]
                    if value_of_triplet > 0:
                        max_value = max(max_value, value_of_triplet)
        return max_value