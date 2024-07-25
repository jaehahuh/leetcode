class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    #search every 1 and increase count by 1
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, x, y):
        if x < 0 or len(grid) <= x or y < 0 or len(grid[0]) <= y or grid[x][y] != "1":
            return
        grid[x][y] = "visited"
        
        #search island horizontally and vertically
        self.dfs(grid,x-1,y)
        self.dfs(grid,x+1,y) 
        self.dfs(grid,x,y-1) 
        self.dfs(grid,x,y+1) 