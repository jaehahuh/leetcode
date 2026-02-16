class Solution:
    def reverseBits(self, n: int) -> int:
        binary_num = bin(n)
        rev_bin = binary_num[2:][::-1]
        length = len(rev_bin)
        rev_bin += '0' * (32-length)        
        return int(rev_bin, 2)