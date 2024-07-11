class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        min_s = min(strs, key=len) #find minimum length of string
        for i, ch in enumerate(min_s):
            for s in strs:
                if s[i] != ch:
                   return answer
            answer += ch

        return answer