class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a)-1, len(b)-1
        
        # Start from the end of both strings
        while i >= 0 or j >= 0 or carry:
        
            current_bit_sum = carry  # Initialize current bit sum with carry
            if i >= 0:
                current_bit_sum += int(a[i])  # Add current bit of a
                i -= 1
            if j >= 0:
                current_bit_sum  += int(b[j])  # Add current bit of b
                j -= 1
        
            # Calculate current bit and carry for the next place
            result.append(str(current_bit_sum  % 2))  # Current bit result
            carry = current_bit_sum // 2   # Carry for the next place

        return ''.join(result[::-1]) # Reverse the result