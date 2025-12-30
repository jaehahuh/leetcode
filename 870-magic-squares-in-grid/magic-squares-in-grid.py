class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic_square(grid, r, c):
            seen_nums = set()
            # Check distinct nums
            for i in range(3):
                for j in range(3):
                    num = grid[r + i][c + j]
                    if not (1 <= num <= 9) or num in seen_nums:
                        return False
                    seen_nums.add(num)
            
            magic_sum = 15
            # Check row sum
            if not (grid[r][c] + grid[r][c+1] + grid[r][c+2] == magic_sum):
                return False
            if not (grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == magic_sum):
                return False
            if not (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == magic_sum):
                return False
            # Check col sum
            if not (grid[r][c] + grid[r+1][c] + grid[r+2][c] == magic_sum): 
                return False
            if not (grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == magic_sum): 
                return False
            if not (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == magic_sum): 
                return False

            # Check diagonal sum
            if not (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == magic_sum): 
                return False
            if not (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == magic_sum): 
                return False
            
            return True
            
        row = len(grid)
        col = len(grid[0])
        if row < 3 and col < 3:
            return 0
        
        magic_squares = 0

        for r in range(row-2):
            for c in range(col-2):
                if is_magic_square(grid, r, c):
                    magic_squares += 1
        
        return magic_squares