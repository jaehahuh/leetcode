class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        dia = defaultdict(list)

        for i in range(n):
            for j in range(n):
                d = i - j
                dia[d].append(grid[i][j])
        
        for d, arr in dia.items():
            if d < 0:
                arr.sort()
                dia[d] = deque(arr) 
            else:
                arr.sort(reverse=True)
                dia[d] = deque(arr)

        for i in range(n):
            for j in range(n):
                d = i-j
                grid[i][j] = dia[d].popleft()
           
        return grid