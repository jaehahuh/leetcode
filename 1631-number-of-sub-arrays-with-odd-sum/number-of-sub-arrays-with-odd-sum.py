class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        curr_sum = 0
        odd_count = 0
        even_count = 0
        result = 0

        for num in arr:
            curr_sum += num
            if curr_sum % 2: #odd case
                result = (result + 1 + even_count) % MOD
                odd_count += 1
            else: # even case
                result = (result + odd_count) % MOD
                even_count += 1

        return result 
