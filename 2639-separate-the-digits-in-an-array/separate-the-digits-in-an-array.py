class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            num = str(num)
            for s in num:
                result.append(int(s))
        return result