class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        num = 0
        for i in range(len(s)-1):
            if table[s[i]] < table[s[i+1]]:
                num = num - table[s[i]]
            else:
                num = num + table[s[i]]
        
        num += table[s[-1]]
        return num