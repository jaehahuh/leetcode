class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        
        is_sorted_between_rows = [False] * (rows - 1)
        
        delete_col_count = 0
        
        for c in range(cols):
            should_delete_current_col = False
            
            for r in range(rows - 1):
                if is_sorted_between_rows[r]:
                    continue
                
                if strs[r][c] > strs[r + 1][c]:
                    should_delete_current_col = True
                    delete_col_count += 1
                    break 
            
            if not should_delete_current_col:
                for r in range(rows - 1):
                    if not is_sorted_between_rows[r] and \
                       strs[r][c] < strs[r + 1][c]:
                        is_sorted_between_rows[r] = True
            
            if all(is_sorted_between_rows):
                break
                
        return delete_col_count