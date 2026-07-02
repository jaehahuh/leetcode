class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_nums = Counter(nums)
        for num, count in count_nums.items():
            if count == 1:
                return num