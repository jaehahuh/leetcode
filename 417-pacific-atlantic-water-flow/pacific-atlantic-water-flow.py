class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]

        def dfs(r, c, reachable_map, prev_height):
            # Base cases:
            # 1. Out of bounds
            # 2. Already marked as reachable from this ocean
            # 3. Current cell's height is lower than the previous cell's height (cannot "flow up" to it)
            if not (0 <= r < m and 0 <= c < n) or reachable_map[r][c] or heights[r][c] < prev_height:
                return
            
            reachable_map[r][c] = True

            # Explore all 4 adjacent directions
            dfs(r + 1, c, reachable_map, heights[r][c]) # down
            dfs(r - 1, c, reachable_map, heights[r][c]) # up
            dfs(r, c + 1, reachable_map, heights[r][c]) # right
            dfs(r, c - 1, reachable_map, heights[r][c]) # left

        # Iterate through rows for left/right borders
        for r in range(m):
            # Pacific border (first column): (r, 0)
            dfs(r, 0, pacific_reachable, -1)
            # Atlantic border (last column): (r, n-1)
            dfs(r, n-1, atlantic_reachable, -1)

        # Iterate through columns for top/bottom borders
        for c in range(n):
            # Pacific border (first row): (0, c)
            dfs(0, c, pacific_reachable, -1)
            # Atlantic border (last row): (m-1, c)
            dfs(m-1, c, atlantic_reachable, -1)

        result = []
        for r in range(m):
            for c in range(n):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])
        
        return result