class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total_laser = 0
        prev_row = 0
        for row in bank:
            curr_row = row.count('1')
            if curr_row > 0:
                if prev_row > 0:
                    total_laser += prev_row * curr_row
                prev_row = curr_row
                
        return total_laser