class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        x = 0
        while True:
            if 3**x > n:
                return False
            elif 3**x == n:
                return True
            x += 1