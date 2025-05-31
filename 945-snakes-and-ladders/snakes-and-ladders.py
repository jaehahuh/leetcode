class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue = deque([(1, 0)])  # (curr_position, number of move)
        visited = set()

        # Convert square number to (row, col) coordinates
        def get_coordinate(pos):
            row_index_from_bottom, col_index_in_row = divmod(pos - 1, n)
        
            # Convert from bottom-based row index to top-based board row index
            row = n - 1 - row_index_from_bottom

            # Determine column index based on the direction of the row (left-to-right or right-to-left)
            if row_index_from_bottom % 2 == 0:
                col = col_index_in_row  # Left to right
            else:
                col = n - 1 - col_index_in_row  # Right to left

            return row, col
        
        while queue:
            pos, moves = queue.popleft()
            for i in range(1, 7): #roll dice
                next_pos = pos + i
                if next_pos > n * n:
                    continue
                
                row, col = get_coordinate(next_pos)
                if board[row][col] != -1:
                    next_pos = board[row][col] # move to the destination of that snake or ladder
                if next_pos == n * n:
                    return moves + 1
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))

        return -1 