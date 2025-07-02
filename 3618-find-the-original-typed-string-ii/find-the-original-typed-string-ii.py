class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(word)

        blocks = [len(list(group)) for _, group in groupby(word)] # ex) "aaabbcdddd" -> [3, 2, 1, 4]
        
        total_combinations = 1
        for count in blocks:
            total_combinations = (total_combinations * count) % MOD
        
        if len(blocks) >= k:
            return total_combinations
        
        prefix_sum = [1] * k

        for count in blocks:
            dp = [0] * k
            for length in range(1, k):
                dp[length] = prefix_sum[length - 1]
                if length - count - 1 >= 0:
                    dp[length] = (dp[length] - prefix_sum[length - count - 1]) % MOD

            prefix_sum = [0] * k
            prefix_sum[0] = dp[0]
            for i in range(1, k):
                prefix_sum[i] = (prefix_sum[i-1] + dp[i]) % MOD

        return (total_combinations - prefix_sum[k-1]) % MOD