class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row_prefix_sums = [[0] * (n + 1) for _ in range(m)]
        for r in range(m):
            for c in range(n):
                row_prefix_sums[r][c+1] = row_prefix_sums[r][c] + grid[r][c]
        
        col_prefix_sums = [[0] * n for _ in range(m + 1)]
        for c in range(n):
            for r in range(m):
                col_prefix_sums[r+1][c] = col_prefix_sums[r][c] + grid[r][c]

        def get_row_segment_sum(r_idx, c_start, length):
            return row_prefix_sums[r_idx][c_start + length] - row_prefix_sums[r_idx][c_start]

        def get_col_segment_sum(r_start, c_idx, length):
            return col_prefix_sums[r_start + length][c_idx] - col_prefix_sums[r_start][c_idx]

        def is_magic_square(r_start, c_start, k):
            
            diag1_sum = 0
            for i in range(k):
                diag1_sum += grid[r_start + i][c_start + i]
            
            target_sum = diag1_sum

            diag2_sum = 0
            for i in range(k):
                diag2_sum += grid[r_start + i][c_start + k - 1 - i]
            if diag2_sum != target_sum:
                return False

            for i in range(k):
                current_row_sum = get_row_segment_sum(r_start + i, c_start, k)
                if current_row_sum != target_sum:
                    return False
            
            for j in range(k):
                current_col_sum = get_col_segment_sum(r_start, c_start + j, k)
                if current_col_sum != target_sum:
                    return False
            
            return True

        for k in range(min(m, n), 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic_square(r, c, k):
                        return k
        
        return 1