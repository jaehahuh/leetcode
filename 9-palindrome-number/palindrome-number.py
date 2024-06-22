class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        inv_num = num[::-1]
        if num == inv_num:
            return True
        return False