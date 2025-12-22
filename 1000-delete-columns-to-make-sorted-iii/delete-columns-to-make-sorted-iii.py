class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])

        dp = [1] * cols

        for c in range(cols):
            for i in range(c):
                is_valid = True
                for r in range(rows):
                    if strs[r][i] > strs[r][c]:
                        is_valid = False
                        break
                
                if is_valid:
                    dp[c] = max(dp[c], dp[i] + 1)

        if not dp:
            max_kept_columns = 0
        else:
            max_kept_columns = max(dp)

        return cols - max_kept_columns 