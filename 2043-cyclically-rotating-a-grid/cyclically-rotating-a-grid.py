class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            top, left = layer, layer
            bottom, right = m - layer - 1, n - layer - 1

            #Current layer's values (rotate clockwise)
            values = []
            # top row
            for i in range(left, right + 1):
                values.append(grid[top][i])
            # right column
            for i in range(top + 1, bottom):
                values.append(grid[i][right])
            # bottom row
            for i in range(right, left-1, -1):
                values.append(grid[bottom][i])
            # left column
            for i in range(bottom-1, top, -1):
                values.append(grid[i][left])
            
            # Rotate counter clockwise k
            l = len(values)
            shift = k % l
            if shift != 0:
                values = values[shift:] + values[:shift]
 
            # Fill up grid
            i = 0 # index of values
            for j in range(left, right + 1):
                grid[top][j] = values[i]
                i += 1
            for j in range(top + 1, bottom):
                grid[j][right] = values[i]
                i += 1
            for j in range(right, left - 1, -1):
                grid[bottom][j] = values[i]
                i += 1
            for j in range(bottom - 1, top, -1):
                grid[j][left] = values[i]
                i += 1
        
        return grid