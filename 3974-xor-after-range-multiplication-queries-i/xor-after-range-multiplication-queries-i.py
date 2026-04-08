class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        for q in queries:
            l, r, k, v = q
            for idx in range(l, r + 1, k):
                nums[idx] = (nums[idx] * v) % MOD
    
        result = 0
        for num in nums:
            result ^= num
        return result