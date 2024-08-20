class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        #use xor method
        bit_flips = start ^ goal
        count = bin(bit_flips).count('1')
        
        return count