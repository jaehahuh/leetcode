class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        def alternate(start_parity):
            count = 0
            expected = start_parity
            for num in nums:
                if num % 2 == expected:
                    count += 1
                    expected ^= 1 # Toggle expected parity (0 <-> 1)
            return count

        # All elements have the same parity
        count_even = sum(1 for num in nums if num % 2 == 0)
        count_odd = n - count_even
        max_mono_len = max(count_even, count_odd) # Max length for same parity subsequences
        
        # Elements alternate in parity
        max_alt_len = max(alternate(0), alternate(1)) # Max length for alternating parity subsequences

        return max(max_mono_len, max_alt_len)