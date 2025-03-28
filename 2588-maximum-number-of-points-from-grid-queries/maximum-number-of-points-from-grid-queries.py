class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        answer = [0] * len(queries)
        row, col = len(grid), len(grid[0])

        indexed_queries = sorted((num, i) for i, num in enumerate(queries))
        visited = set([(0, 0)])
        min_heap = [(grid[0][0], 0 , 0)] # (value, row, col))
        points = 0

        for limit, index in indexed_queries:
            # Explore cells while the min-heap has values less than the query limit
            while min_heap and min_heap[0][0] < limit:
                value, r, c = heappop(min_heap)
                points += 1 

                # Explore neighboring cells
                neighbors = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
                for nei_r, nei_c in neighbors:
                    if 0 <= nei_r < row and 0 <= nei_c < col and (nei_r, nei_c) not in visited:
                        heappush(min_heap, (grid[nei_r][nei_c], nei_r, nei_c))
                        visited.add((nei_r, nei_c))

            # Store the score for the current query
            answer[index] = points
        return answer