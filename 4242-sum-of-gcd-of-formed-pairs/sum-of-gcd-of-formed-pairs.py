class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = []

        curr_max = 0
        for num in nums:
            if num > curr_max:
                curr_max = num
            prefixGcd.append(math.gcd(num, curr_max))
        
        prefixGcd.sort()
        total = 0
        left, right = 0, n-1

        while left < right:
            total += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        
        return total