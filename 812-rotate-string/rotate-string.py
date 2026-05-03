class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        double_s = s + s
        n = len(s)
        for i in range(n):
            if double_s[i:i+n] == goal:
                return True
        return False