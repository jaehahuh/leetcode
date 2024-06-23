class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_str = min(strs, key=len)
        for i, ch in enumerate(min_str):
            for s in strs:
                if s[i] != ch:
                    return min_str[:i]
        return min_str
