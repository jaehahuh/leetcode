class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        max_coord = 51 # 0 ~ 50

        grid = [[0] * max_coord for _ in range(max_coord)]
        for x, y in points:
            grid[x][y] = 1

        prefix_sum = [[0] * (max_coord + 1) for _ in range(max_coord + 1)]
        for x in range(max_coord):
            row_sum = 0
            for y in range(max_coord):
                row_sum += grid[x][y]
                prefix_sum[x+1][y+1] = prefix_sum[x][y+1] + row_sum

            def rect_sum(x1, y1, x2, y2):
            # 모두 경계 포함, x1 <= x2, y1 <= y2 가정
                return prefix_sum[x2 + 1][y2 + 1] - prefix_sum[x1][y2 + 1] - prefix_sum[x2 + 1][y1] + prefix_sum[x1][y1]

        n = len(points)
        result = 0
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]

                # A is on the upper left side of B
                if not (x1 <= x2 and y1 >= y2):
                    continue

                # rectangle (including the border) 
                xl, xr = (x1, x2) if x1 <= x2 else (x2, x1)
                yl, yr = (y2, y1) if y2 <= y1 else (y1, y2)  
                if rect_sum(xl, yl, xr, yr) == 2:
                    result += 1

        return result