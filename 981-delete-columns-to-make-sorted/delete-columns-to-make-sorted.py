class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        rows = len(strs) 
        cols = len(strs[0])
        columns_string = ['' for _ in range(cols)]
        for r in range(rows):
            s = strs[r]
            for c in range(cols):
                columns_string[c] += s[c]
        
        for col_s in columns_string:
            for i in range(1, len(col_s)):
                if col_s[i] < col_s[i-1]:
                    result += 1
                    break

        return result       