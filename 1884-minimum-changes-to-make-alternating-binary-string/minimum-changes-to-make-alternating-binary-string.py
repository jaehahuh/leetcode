class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        start_with_zero = 0
        start_with_one = 0
        
        for i, char in enumerate(s):
            expected_char_zero = '0' if i % 2 == 0 else '1'
            expected_char_one = '1' if i % 2 == 0 else '0'

            if char != expected_char_zero:
                start_with_zero += 1

            if char != expected_char_one:
                start_with_one += 1
        
        return min(start_with_zero, start_with_one)