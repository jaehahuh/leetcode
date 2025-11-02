class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0]*n for _ in range(m)] # 0: empty
        for r,c in guards:
            grid[r][c] = 1
        for r,c in walls:
            grid[r][c] = 2

        guarded = [[False]*n for _ in range(m)]

        # Rows: left->right and right->left
        for i in range(m):
            seen_guard = False
            for j in range(n):
                if grid[i][j] == 1:  # guard
                    seen_guard = True
                elif grid[i][j] == 2:  # wall
                    seen_guard = False
                elif seen_guard:
                    guarded[i][j] = True

            seen_guard = False
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    seen_guard = True
                elif grid[i][j] == 2:
                    seen_guard = False
                elif seen_guard:
                    guarded[i][j] = True

        # Columns: top->bottom and bottom->top
        for j in range(n):
            seen_guard = False
            for i in range(m):
                if grid[i][j] == 1:
                    seen_guard = True
                elif grid[i][j] == 2:
                    seen_guard = False
                elif seen_guard:
                    guarded[i][j] = True

            seen_guard = False
            for i in range(m-1, -1, -1):
                if grid[i][j] == 1:
                    seen_guard = True
                elif grid[i][j] == 2:
                    seen_guard = False
                elif seen_guard:
                    guarded[i][j] = True

        # Count unguarded empty cells
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not guarded[i][j]:
                    result += 1
        return result