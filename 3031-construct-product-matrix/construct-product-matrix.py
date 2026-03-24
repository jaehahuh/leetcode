class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        result = [[0] * m for _ in range(n)]
        prefix_product = 1
        for i in range(n):
            for j in range(m):
                result[i][j] = prefix_product
                prefix_product = (prefix_product * grid[i][j]) % MOD
        
        suffix_product = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                result[i][j] = (result[i][j] * suffix_product) % MOD
                suffix_product = (suffix_product * grid[i][j]) % MOD

        return result