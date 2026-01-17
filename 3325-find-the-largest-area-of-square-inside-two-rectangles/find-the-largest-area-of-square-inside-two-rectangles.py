class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_area = 0
        for i in range(n):
            for j in range(i + 1, n):
                # First rectangle's coordinates
                x1_i, y1_i = bottomLeft[i]
                x2_i, y2_i = topRight[i]
                
                # Second rectangle's coordinates
                x1_j, y1_j = bottomLeft[j]
                x2_j, y2_j = topRight[j]

                intersect_x1 = max(x1_i, x1_j)
                intersect_y1 = max(y1_i, y1_j)
                intersect_x2 = min(x2_i, x2_j)
                intersect_y2 = min(y2_i, y2_j)

                if intersect_x1 < intersect_x2 and intersect_y1 < intersect_y2:
                    width = intersect_x2 - intersect_x1
                    height = intersect_y2 - intersect_y1

                    side = min(width, height)
                    max_area = max(max_area, side * side)
                    
        return max_area