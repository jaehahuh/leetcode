class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        def get_divisors(length):
            divs = []
            for d in range(1, length):
                if length % d == 0:
                    divs.append(d)
            return divs

        def get_group_cost(sub, d):
            length = len(sub)
            group_len = length // d
            total_changes = 0

            for g in range(d):
                left = g
                right = g + (group_len - 1) * d

                while left < right:
                    if sub[left] != sub[right]:
                        total_changes += 1

                    left += d
                    right -= d

            return total_changes

        # Precompute substring costs
        cost = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            divs = get_divisors(length)

            for i in range(n - length + 1):
                j = i + length - 1
                sub = s[i:j + 1]

                min_c = float("inf")

                for d in divs:
                    min_c = min(
                        min_c,
                        get_group_cost(sub, d)
                    )

                cost[i][j] = min_c

        # Partition DP
        dp = [[float("inf")] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    dp[p][i] = min(
                        dp[p][i],
                        dp[p - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]