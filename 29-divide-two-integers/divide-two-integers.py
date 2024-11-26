class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_max = 2**31 - 1
        int_min = -2**31

        sign = -1 if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else 1
        
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            # Initialize currentDivisor to divisor and numDivisor to count how many times we can subtract
            currentDivisor, numDivisor = divisor, 1  
            while dividend >= currentDivisor:
                dividend -= currentDivisor
                quotient += numDivisor
                currentDivisor <<= 1 # Double the currentDivisor (shift left by 1)
                numDivisor <<= 1 # Double the numDivisor (shift left by 1)
        
        quotient *= sign
        
        if quotient < int_min:
            return int_min
        if quotient > int_max:
            return int_max
    
        return quotient