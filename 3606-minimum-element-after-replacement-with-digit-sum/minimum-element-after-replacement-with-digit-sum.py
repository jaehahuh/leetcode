class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_element = 37 # Since limit is 9999 = 36, set the maximum to 37
        for n in nums:
            digit_sum = 0
            while n > 0:
                digit_sum += n%10
                n //= 10
            min_element = min(min_element, digit_sum)
        return min_element