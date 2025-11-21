class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        palin_sub = set()
        left = set()
        right = Counter(s)

        for mid_ch in s:
            right[mid_ch] -= 1
            for outer_ch in left:
                if right[outer_ch] > 0:
                    palin_sub.add((mid_ch ,outer_ch))
            left.add(mid_ch)
    
        return len(palin_sub)