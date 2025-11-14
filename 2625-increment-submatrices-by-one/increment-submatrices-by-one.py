class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * (n+1) for _ in range(n+1)]
        
        for r1, c1, r2, c2 in queries:
            matrix[r1][c1] += 1
            matrix[r1][c2 + 1] -= 1
            matrix[r2+1][c1] -= 1
            matrix[r2+1][c2 + 1] += 1
        
        for i in range(n):
            running = 0
            for j in range(n):
                running += matrix[i][j]
                matrix[i][j] = running
        
        result = [[0] * n for _ in range(n)]
        for j in range(n):
            running = 0
            for i in range(n):
                running += matrix[i][j]
                result[i][j] = running

        return result