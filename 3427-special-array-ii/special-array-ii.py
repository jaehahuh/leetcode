class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        parity = [num % 2 for num in nums]  # Create a Parity Array
        special_prefix = [0] * (n + 1)  # Count of intervals with the same consecutive parity

        for i in range(1, n):
            if parity[i] == parity[i - 1]:
                special_prefix[i] = 1  # Increase the count if continuous parity is the same
        
        for i in range(1, n):
            special_prefix[i] += special_prefix[i - 1]

        res = [special_prefix[i] - special_prefix[j] == 0 for i, j in queries] #i = from, j = to in queries
        return res       