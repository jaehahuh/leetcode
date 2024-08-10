class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_lst = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            count_lst.append(count)
        return count_lst