class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = 0

        for j in range(1, len(nums)-1):
            max_i = max(nums[:j])  # max nums[i] before nums[j]
            max_k = max(nums[j+1:]) # max nums[k] after nums[j]
            value_of_triplet = (max_i - nums[j]) * max_k

            if value_of_triplet > max_value:
                max_value = value_of_triplet
        return max_value