class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        msb_index = n.bit_length() - 1  #most siginifcant bit index
        msb_value = 1 << msb_index
        x = (1 << (msb_index + 1)) - 1 
        remainder = n - msb_value
        return x - self.minimumOneBitOperations(remainder)