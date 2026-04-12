from functools import lru_cache
    
class Solution:
    def minimumDistance(self, word: str) -> int:
    
        # 알파벳의 좌표 매핑 (0~25)
        coords = {}
        rows = ["ABCDEF",
                "GHIJKL",
                "MNOPQR",
                "STUVWX",
                "YZ"]
        for i, row in enumerate(rows):
            for j, ch in enumerate(row):
                coords[ch] = (i, j)
        
        def dist(a, b):
            if a == -1 or b == -1:
                return 0
            x1, y1 = coords[chr(a + ord('A'))]
            x2, y2 = coords[chr(b + ord('A'))]
            return abs(x1 - x2) + abs(y1 - y2)
        
        @lru_cache(None)
        def dp(i, f1, f2):
            if i == len(word):
                return 0
            
            cur = ord(word[i]) - ord('A')
            
            # 손가락1 이동
            cost1 = dist(f1, cur) + dp(i + 1, cur, f2)
            # 손가락2 이동
            cost2 = dist(f2, cur) + dp(i + 1, f1, cur)
            
            return min(cost1, cost2)
        
        return dp(0, -1, -1)