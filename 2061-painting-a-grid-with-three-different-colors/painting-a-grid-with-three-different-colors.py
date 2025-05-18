class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        colors = [0, 1, 2] #red, green, blue

        def valid(col):
            return all(col[i] != col[i+1] for i in range(len(col)-1))

        states = [col for col in product(colors, repeat=m) if valid(col)]
        state_indices = {state: i for i, state in enumerate(states)}
        k = len(states)  # number of valid states

        can_follow = [[] for _ in range(k)]

        for i, s1 in enumerate(states):
            for j, s2 in enumerate(states):
                if all(a != b for a, b in zip(s1, s2)):
                    can_follow[i].append(j)

        dp = [1] * k 

        for _ in range(n - 1):
            new_dp = [0] * k
            for i in range(k):
                for j in can_follow[i]: 
                    new_dp[i] = (new_dp[i] + dp[j]) % MOD
            dp = new_dp

        return sum(dp) % MOD