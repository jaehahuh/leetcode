class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda x : (x[0], -x[1]))
        result = 0

        for i in range(n):
            x1, y1 = points[i]
            maxY = -float('inf') # 지금까지 본 후보들 중 y의 최댓값

            # i보다 오른쪽(같은 x 포함) 점들만 확인
            for j in range(i+1, n):
                x2, y2 = points[j]

                if y2 > y1:  # 다음 y값이 이전 y값보다 크면 넘어감
                    continue
                
                if y2 > maxY: 
                    result += 1
                    maxY = y2
        
        return result