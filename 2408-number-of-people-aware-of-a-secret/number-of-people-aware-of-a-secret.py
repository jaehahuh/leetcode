class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7

        dp = [0] * (n + 1)
        dp[1] = 1

        current_sharing_people = 0
        total_aware_people = 1

        for i in range(2, n + 1):
            if i - delay >= 1:
                current_sharing_people = (current_sharing_people + dp[i - delay]) % MOD

            if i - forget >= 1:
                current_sharing_people = (current_sharing_people - dp[i - forget] + MOD) % MOD
                total_aware_people = (total_aware_people - dp[i - forget] + MOD) % MOD

            dp[i] = current_sharing_people
            total_aware_people = (total_aware_people + dp[i]) % MOD
        
        return total_aware_people