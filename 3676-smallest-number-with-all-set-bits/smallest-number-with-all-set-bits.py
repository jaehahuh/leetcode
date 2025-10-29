class Solution:
    def smallestNumber(self, n: int) -> int:
        bit_num = bin(n)
        bit_num = bit_num[2:]
        bin_x = len(bit_num) * '1'
        x = int(bin_x, 2)
        return x