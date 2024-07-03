class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        answer = ''
        #Time complexity is actually size of s
        for row in range(numRows):
            increment = 2*(numRows - 1) 
            for i in range(row, len(s), increment): 
                #it works for all rows
                answer += s[i] 
                #it apply all rows except first and last row
                if (row > 0 and row < numRows - 1 and (i + increment - 2 * row) < len(s)):
                    answer += s[i + increment - 2 * row]
        
        return answer