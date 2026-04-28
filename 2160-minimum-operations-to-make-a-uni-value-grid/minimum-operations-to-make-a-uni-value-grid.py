class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flattened = [element for row in grid for element in row]
        mod = flattened[0] % x
        for num in flattened:
            if num % x != mod:
                return -1
        flattened.sort()
        n = len(flattened)
        median = flattened[n//2]

        min_op = 0
        for num in flattened:
            min_op += abs(num - median)//x
        
        return min_op