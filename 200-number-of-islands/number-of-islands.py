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

    def dfs(self, grid, v, h):
        if v < 0 or len(grid) <= v or h < 0 or len(grid[0]) <= h or grid[v][h] != "1":
            return
        grid[v][h] = "visited"

        #search island horizontally and vertically
        self.dfs(grid, v-1, h)
        self.dfs(grid, v+1, h) 
        self.dfs(grid, v, h-1) 
        self.dfs(grid, v, h+1) 