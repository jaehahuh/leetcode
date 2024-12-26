class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums) #total number of elements in array
        dp = defaultdict(int)

        dp[0] = 1 # (0 sum) -> 1 way
        for i in range(n):
            next_dp = defaultdict(int)
            for curr_sum, count in dp.items():
                next_dp[curr_sum + nums[i]] += count
                next_dp[curr_sum - nums[i]] += count
            dp = next_dp #replace with updated dp

        #returns the number of cases with a target sum
        return dp[target] 