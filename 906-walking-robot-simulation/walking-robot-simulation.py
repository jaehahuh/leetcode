class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))
        # N, E, S, W
        dx = [0, 1, 0, -1] 
        dy = [1, 0, -1, 0]

        x = y = direction = 0
        max_dist = 0

        for num in commands:
            if num == -2: # Turn left
                direction = (direction - 1) % 4
            elif num == -1: # Turn right
                direction = (direction + 1) % 4
            else: 
                # Move each step
                for _ in range(num):
                    nx, ny = x + dx[direction], y + dy[direction]
            
                    if (nx, ny) in obstacle_set:
                        break
                    
                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)
                
        return max_dist