class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = [(startx, endx) for startx, starty, endx, endy in rectangles]
        y = [(starty, endy) for startx, starty, endx, endy in rectangles]

        x.sort()
        y.sort()

        def check_cuts(intervals):
            count = 0
            prev_end = -1
            for start, end in intervals:
                if prev_end <= start:
                    count += 1
                prev_end = max(prev_end, end)
            return count
        
        return max(check_cuts(x), check_cuts(y)) >= 3