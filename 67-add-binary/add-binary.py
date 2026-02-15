class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a)-1, len(b)-1
        while i >= 0 or j >= 0 or carry:
            current_bit_sum = carry
            if i >= 0:
                current_bit_sum += int(a[i])
                i -= 1
            if j >= 0:
                current_bit_sum += int(b[j])
                j -= 1

            result.append(str(current_bit_sum % 2))  
            carry = current_bit_sum // 2   

        return ''.join(result[::-1]) 