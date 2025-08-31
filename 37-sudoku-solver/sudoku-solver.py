class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = len(board) #9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        empty = []
        for i in range(n):
            for j in range(n):
                ch = board[i][j]
                if ch == '.':
                    empty.append((i, j))
                else:
                    box = (i//3) * 3 + (j//3)
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[box].add(ch)

        def backtracking(index):
            if index == len(empty):
                return True
            i, j = empty[index]
            box = (i//3) * 3 + (j//3)

            for ch in '123456789':
                if ch not in rows[i] and ch not in cols[j] and ch not in boxes[box]:
                    board[i][j] = ch
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[box].add(ch)

                    if backtracking(index + 1):
                        return True
                    
                    board[i][j] = '.'
                    rows[i].remove(ch)
                    cols[j].remove(ch)
                    boxes[box].remove(ch)
            
            return False
        
        backtracking(0)