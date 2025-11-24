class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        curr_remain = 0
        for num in nums:
            curr_remain = (curr_remain * 2 + num) % 5
            if curr_remain == 0:
                result.append(True)
            else:
                result.append(False)
        return result