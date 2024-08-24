class Solution:
    def minSteps(self, n: int) -> int:
        # Initialize the dp array with a large number (1000: constraints)
        # dp[i] will represent the minimum number of operations to get exactly i 'A's on the screen.
        dp = [1000] * (n+1)

        # Base case: To have 1 'A' on the screen, no operations are needed.
        dp[1] = 0
        
        # iterate from 2 to n to calculate the minimum steps for each i.
        for i in range(2, n+1):
            # check all possible divisors j of i (j <= i // 2).
            # if j divides i, then we can achieve i 'A's by first getting j 'A's
            # and then performing (i // j) paste operations.
            for j in range(1, 1+(i//2)):
                if i % j == 0:
                    # update dp[i] as the minimum of current dp[i] or operations 
                    # to get j 'A's plus (i // j) pastes.
                    dp[i] = min(dp[i], dp[j] + i//j)

        #final answer is stored in dp[n], which gives the minimum steps to get n 'A's
        return dp[n]