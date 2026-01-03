class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        prev_2color = 6 #(RYR, RGR, YRY, YGY, GRG, GYG)
        prev_3color = 6 #(RYG, RGY, YRG, YGR, GRY, GYR)

        for i in range(2, n + 1):
            curr_2color = (3 * prev_2color + 2 * prev_3color) % MOD
            curr_3color = (2 * prev_2color + 2 * prev_3color) % MOD

            prev_2color = curr_2color
            prev_3color = curr_3color
       
        return (prev_2color + prev_3color) % MOD