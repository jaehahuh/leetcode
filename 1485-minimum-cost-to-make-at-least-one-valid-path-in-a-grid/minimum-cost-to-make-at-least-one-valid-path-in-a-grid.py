class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = {
            1: (0, 1),   # right
            2: (0, -1),  # left
            3: (1, 0),   # down
            4: (-1, 0)   # up
        }
        rows, columns = len(grid), len(grid[0])
        q = deque([(0, 0, 0)]) #(row, col, cost)

        # Dictionary to store the minimum cost to reach each cell
        min_cost = {(0,0):0}

        #BFS
        while q:
            r, c, cost = q.popleft()

            # If we reach the bottom-right corner, return the cost
            if (r, c) == (rows - 1, columns - 1):
                return cost
            
            for d in directions:
                dr, dc = directions[d]
                nr, nc = r + dr, c + dc #neighbor row and column

                #If the direction matches the grid value, the cost remains the same
                #Otherwise, increment the cost by 1 for modifying the direction
                new_cost = cost if d == grid[r][c] else cost + 1

                #Skip invalid positions or if the cost to reach the neighbor cell
                #is greater than or equal to the current minimum cost for that cell
                if (nr < 0 or nc < 0 or nr == rows or nc == columns or new_cost >= min_cost.get((nr, nc), float("inf"))):
                    continue
                
                # Update the minimum cost to reach the neighbor cell
                min_cost[(nr, nc)] = new_cost
                if d == grid[r][c]:
                    q.appendleft((nr, nc, new_cost))
                else:
                    q.append((nr, nc, new_cost))