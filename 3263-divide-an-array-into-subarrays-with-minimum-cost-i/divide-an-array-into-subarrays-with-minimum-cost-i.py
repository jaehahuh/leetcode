class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first_elem = nums[0]
        nums.sort()
        if first_elem == nums[0]:
            return first_elem + nums[1] + nums[2]
        elif first_elem == nums[1]:
            return  first_elem + nums[0] + nums[2]
        else:
            return first_elem + nums[0] + nums[1]