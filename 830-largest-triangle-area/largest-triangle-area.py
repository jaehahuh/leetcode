class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        max_area = 0.0

        for i in range(n-2):
            for j in range(i + 1, n-1):
                for k in range(j + 1, n):
                    p1 = points[i]
                    p2 = points[j]
                    p3 = points[k]

                    # Area = 0.5 * |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|
                    area = 0.5 * abs(p1[0] * (p2[1] - p3[1]) +  # x1 * (y2 - y3)
                                     p2[0] * (p3[1] - p1[1]) +  # x2 * (y3 - y1)
                                     p3[0] * (p1[1] - p2[1]))   # x3 * (y1 - y2)

                    max_area = max(max_area, area)
            
        return max_area