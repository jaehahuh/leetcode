class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        def square_sum(r1, c1, r2, c2):
            return sum_mat[r2 + 1][c2 + 1] - sum_mat[r1][c2 + 1] - sum_mat[r2 + 1][c1] + sum_mat[r1][c1]
        def check(side):
            if side == 0:
                return True
            for r in range(m - side + 1):
                for c in range(n - side + 1):
                    r_end, c_end = r + side - 1, c + side - 1
                    current_sum = square_sum(r, c, r_end, c_end)
                
                    if current_sum <= threshold:
                        return True
            return False

        m,n = len(mat), len(mat[0])
        sum_mat = [[0] * (n+1) for _ in range(m+1)]
        for r in range(m):
            for c in range(n):
                sum_mat[r+1][c+1] = mat[r][c] + sum_mat[r][c + 1] + sum_mat[r + 1][c] - sum_mat[r][c]
        
        low = 0
        high = min(m, n) 
        max_side = 0

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                max_side = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return max_side