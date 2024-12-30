class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        points.sort() # sort the points by x-coordinate
        result = []
        for xj,yj,rj in queries:
            count = 0
            for xi,yi in points: 
                if xi < xj - rj: #if xi outside the left range of the circle
                    continue
                if xi > xj + rj: #if xi outside the right range of the circle
                    break
                if (xi - xj) ** 2 + (yi - yj) ** 2 <= rj ** 2:
                    count += 1
            result.append(count)
        return result