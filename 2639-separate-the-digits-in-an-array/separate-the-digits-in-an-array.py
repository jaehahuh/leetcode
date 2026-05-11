class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            digits = deque()
            while num > 0:
                digits.appendleft(num%10)
                num = num//10
            result.extend(digits)

        return result