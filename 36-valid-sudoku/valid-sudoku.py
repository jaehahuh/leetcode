class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                ch = board[i][j]
                if ch == '.':
                    continue
                box = (i//3) * 3 + (j//3)
                if ch in rows[i] or ch in cols[j] or ch in boxes[box]:
                    return False
                
                rows[i].add(ch)
                cols[j].add(ch)
                boxes[box].add(ch)
                
        return True