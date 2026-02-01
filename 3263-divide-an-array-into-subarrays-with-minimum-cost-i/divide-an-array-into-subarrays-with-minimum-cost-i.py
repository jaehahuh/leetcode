class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first_elem = nums[0]
        rest_elems = nums[1:]
        rest_elems.sort()
        
        return first_elem  + rest_elems[0] + rest_elems[1]