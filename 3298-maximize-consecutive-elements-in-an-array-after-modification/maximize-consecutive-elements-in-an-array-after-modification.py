class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        max_len = 0

        for x in nums:
            dp[x + 1] = dp[x] + 1
            dp[x] = dp[x - 1] + 1
            max_len = max(max_len, dp[x], dp[x + 1])

        return max_len