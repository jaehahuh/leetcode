class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7

        def dfs(lst):
            if len(lst) <= 2:
                return 1
            
            root = lst[0]
            left = [x for x in lst[1:] if x < root]
            right = [x for x in lst[1:] if x > root]

            l, r = len(left), len(right)
            ways = math.comb(l + r, l) * dfs(left) * dfs(right)
            return ways % MOD
    
        return (dfs(nums) - 1) % MOD