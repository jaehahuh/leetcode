class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp[r][c][remainder]
        dp = [[[0 for _ in range(k)] for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1 # Base case

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0: # Skip start cell, already initialized
                    continue
                # Get the remainder of current cell's value when divided by k
                current_val_mod_k = grid[r][c] % k
                for target_rem in range(k):
                    # Calculate the remainder needed from the previous cell (up or left)
                    # (prev_rem + current_val_mod_k) % k == target_rem
                    needed_prev_rem = (target_rem - current_val_mod_k + k) % k
                    # Add paths coming from the cell above (r-1, c)
                    if r > 0:
                        dp[r][c][target_rem] = (dp[r][c][target_rem] + dp[r-1][c][needed_prev_rem]) % MOD
                    # Add paths coming from the cell to the left (r, c-1)
                    if c > 0:
                        dp[r][c][target_rem] = (dp[r][c][target_rem] + dp[r][c-1][needed_prev_rem]) % MOD

        return dp[m-1][n-1][0]