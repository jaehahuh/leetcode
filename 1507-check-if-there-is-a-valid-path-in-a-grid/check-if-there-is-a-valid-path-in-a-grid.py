class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        moves = {# direction, possible cell's street
            1: [(0, -1, [1,4,6]), (0, 1, [1,3,6])], # moves left or right
            2: [(-1, 0, [2,3,4]), (1, 0, [2,5,6])], # moves up or down
            3 : [(0, -1, [1,4,6]), (1, 0, [2,5,6])],  
            4: [(0, 1, [1,3,5]), (1, 0, [2,5,6])],   
            5: [(0, -1, [1,4,6]), (-1, 0, [2,3,4])],
            6: [(0, 1, [1,3,5]), (-1, 0, [2,3,4])]   
            }
        
        visited = [[False]*cols for _ in range(rows)]
        queue = deque([(0,0)])
        visited[0][0] = True

        while queue:
            x, y = queue.popleft()
            if x == rows - 1 and y == cols - 1: # if reached the bottom-right cell
                return True

            # Check all possible moves for current cell's street type
            for dx, dy, valid_next_roads in moves[grid[x][y]]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    if grid[nx][ny] in valid_next_roads:
                        visited[nx][ny] = True
                        queue.append((nx,ny))
            
        return False