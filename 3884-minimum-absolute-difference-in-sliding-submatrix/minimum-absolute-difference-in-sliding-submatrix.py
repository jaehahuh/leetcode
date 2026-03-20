class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                elements =  set()
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        elements.add(grid[r][c])

                sorted_elements = sorted(list(elements))
                min_diff = float('inf')

                if len(elements) <= 1:
                    min_diff = 0
                else:
                    for index in range(len(sorted_elements)-1):
                        diff = abs(sorted_elements[index] - sorted_elements[index+1])
                        min_diff = min(min_diff, diff)
                        if min_diff == 0: 
                            break
                result[i][j] = min_diff

        return result