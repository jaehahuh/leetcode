class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(i, curr_sum):
            if curr_sum == n:
                return True
            if curr_sum > n or 3 ** i > n:
                return False
            
            # include
            if backtrack(i + 1, curr_sum + 3**i):
                return True
            # skip
            return backtrack(i + 1, curr_sum)

        return backtrack(0, 0)