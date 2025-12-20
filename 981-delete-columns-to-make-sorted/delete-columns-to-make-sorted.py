class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        rows = len(strs) 
        cols = len(strs[0])
        for c in range(cols):
            is_sorted = True
            for r in range(1, rows):
                if strs[r][c] < strs[r-1][c]:
                    is_sorted = False
                    break
            if not is_sorted:
                result += 1
        
        return result   