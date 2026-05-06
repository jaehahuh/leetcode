class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        # Apply Gravity
        for r in range(m):
            empty_pos = n - 1
            for c in range(n-1, -1 , -1):
                if boxGrid[r][c] == '#':
                    boxGrid[r][c], boxGrid[r][empty_pos] = boxGrid[r][empty_pos], boxGrid[r][c]
                    empty_pos -= 1
                elif boxGrid[r][c] == '*':
                    empty_pos = c - 1
        
        # Rotate 90 degrees clockwise
        result = [['' for _ in range(m)] for _ in range(n)]
        for r in range(m):
            for c in range(n):
                result[c][m-1-r] = boxGrid[r][c]
        
        return result