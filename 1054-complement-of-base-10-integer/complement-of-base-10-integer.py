class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_num = bin(n)[2:]
        complement = ''
        for bit in bin_num:
            if bit == '0':
                complement += '1'
            else:
                complement += '0'
        
        return int(complement, 2)