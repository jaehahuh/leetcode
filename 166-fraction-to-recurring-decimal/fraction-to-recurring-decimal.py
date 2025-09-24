class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []
        # Sign part
        if (numerator < 0) != (denominator < 0):
            result.append('-')
        
        n, d = abs(numerator), abs(denominator)

        # Integer part
        integer_part = n//d
        result.append(str(integer_part))

        remainder = n%d
        if remainder == 0:
            return ''.join(result)
        
        # Decimal part
        result.append('.')

        remainder_index = {}
        while remainder != 0:
            # Repeating part
            if remainder in remainder_index:
                index = remainder_index[remainder]
                result.insert(index, '(')
                result.append(')')
                break
            
            # Record the start index of the current place
            remainder_index[remainder] = len(result)

            remainder *= 10
            digit = remainder // d
            result.append(str(digit))
            remainder %= d
        
        return ''.join(result)