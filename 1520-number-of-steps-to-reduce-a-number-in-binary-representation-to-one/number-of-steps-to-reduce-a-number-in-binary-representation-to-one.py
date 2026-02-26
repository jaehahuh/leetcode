class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0

        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i])
            total = bit + carry
            if total == 1: # odd num
                steps += 2
                carry = 1
            else:
                steps += 1
        
        if carry == 1:
            steps += 1
        
        return steps