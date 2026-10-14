class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1 or sum > 9 * num:
            return ""
        
        x = sum // 9
        r = sum % 9

        result = []
        for i in range(x):
            result.append('9')
        
        if r > 0:
            result.append(str(r))
        
        while len(result) < num:
            result.append('0')
    
        return ''.join(result)