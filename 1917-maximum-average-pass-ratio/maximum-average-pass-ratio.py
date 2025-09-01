class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t):
            return (p + 1)/(t + 1) - p/t

        heap = []
        for p, t in classes:
            heapq.heappush(heap, (-gain(p,t), p, t))
    
        for _ in range(extraStudents):
            _ , p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p,t), p, t))

        total = 0.0
        while heap:
            _ , p, t = heapq.heappop(heap)
            total += p/t
        
        max_avg = total/len(classes)
        return max_avg