class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        count = collections.Counter(nums)
        for key, item in count.items():
            if item == n:
                return key