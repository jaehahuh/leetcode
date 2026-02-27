class Solution:
    def minOperations(self, s: str, k: int) -> int:
        def ceil (a, b):
            return (a + b - 1) // b
            
        n = len(s)
        zeros = s.count('0')

        if n == k:
            if zeros == 0:
                return 0
            elif zeros == n:
                return 1
            else:
                return -1

        result = float('inf')

        if zeros % 2 == 0:
            temp_min_ops = max(ceil(zeros,k), ceil(zeros, n-k))
            if temp_min_ops % 2 == 1:
                temp_min_ops += 1
            result = min(result, temp_min_ops)
        
        if zeros % 2 == k % 2:
            temp_min_ops = max(ceil(zeros, k), ceil(n - zeros, n - k))
            if temp_min_ops % 2 == 0:
                temp_min_ops += 1
            result = min(result, temp_min_ops)

        return result if result < float('inf') else -1