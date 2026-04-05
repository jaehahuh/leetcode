class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ud_count = 0
        lr_count = 0

        for m in moves:
            if m == "U":
                ud_count += 1
            elif m == 'D':
                ud_count -= 1
            elif m == 'L':
                lr_count += 1
            else:
                lr_count -= 1
        
        return True if ud_count == 0 and lr_count == 0 else False