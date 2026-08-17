class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
    
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @lru_cache(None)
        def solve(i: int, j: int) -> int:
            if i == j:
                return 0
            
            total_sum = prefix[j + 1] - prefix[i]
            res = 0
            
            for k in range(i, j):
                left_sum = prefix[k + 1] - prefix[i]
                right_sum = total_sum - left_sum

                if left_sum < right_sum:
                    if left_sum + left_sum <= res:
                        continue
                    res = max(res, left_sum + solve(i, k))
                elif left_sum > right_sum:
                    if right_sum + right_sum <= res:
                        continue
                    res = max(res, right_sum + solve(k + 1, j))
                else:
                    res = max(
                        res,
                        left_sum + solve(i, k),
                        right_sum + solve(k + 1, j)
                    )
                    
            return res

        return solve(0, n - 1)