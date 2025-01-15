class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count = bin(num2).count('1') #count bit '1' of num2

        x = 0
        for i in range(31, -1, -1): # 32bits
            if count == 0:
                break
            if num1 & (1 << i): # If the i-th bit of num1 is 1
                x |= (1 << i) # Set the i-th bit of x to 1
                count -= 1 

        # Handle remaining 1 bits
        for i in range(32):  # Check bits from 0 upwards
            if count == 0:
                break
            if not (x & (1 << i)):  # If the i-th bit of x is 0
                x |= (1 << i)  # Set the i-th bit of x to 1
                count -= 1
        
        return x