class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            digits = []
            while num > 0:
                digits.append(num%10)
                num = num//10
            reverse_order = digits[::-1]
            result.extend(reverse_order)

        return result