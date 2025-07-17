class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        max_length = 1
        dp = [[0] * k for _  in range(k)] # dp[mod][curr_rem]

        for num in nums:
            curr_r = num % k # Current number's modulo with k
            for target_mod in range(k):
                prev_r = (target_mod - curr_r + k) % k

                new_length = 1
                # If there is a previous subsequence with (prev + curr) % k == c, we can extend it by adding the current number
                if dp[target_mod][prev_r] > 0:
                    new_length = dp[target_mod][prev_r] + 1
                
                # Update the dp table: for current mod pair (target_mod, curr_r), take max
                dp[target_mod][curr_r] = max(dp[target_mod][curr_r], new_length)

                # Update the global maximum length
                max_length = max(max_length, dp[target_mod][curr_r])
        
        return max_length