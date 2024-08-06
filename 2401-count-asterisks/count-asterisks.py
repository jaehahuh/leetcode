class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        flag = 0
        for ch in s:
            if ch == "*" and flag == 0:
                count += 1
            
            if ch == "|" and flag == 0:
                flag = 1
            elif ch == "|" and flag == 1:
                flag = 0

        return count