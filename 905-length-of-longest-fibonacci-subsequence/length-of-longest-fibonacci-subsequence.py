class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_map = {num:i for i, num in enumerate(arr)}
        dp = {}
        result = 0

        for k in range(len(arr)):
            for j in range(k):
                i = arr_map.get(arr[k]-arr[j])
                if i is not None and i < j:
                    dp[j, k] = 1 + dp.get((i, j), 2)
                    result = max(result, dp[j, k])

        return result if result >= 3 else 0