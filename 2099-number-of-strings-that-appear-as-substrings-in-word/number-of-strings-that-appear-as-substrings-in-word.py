class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        result = 0
        for p in patterns:
            if p in word:
                result += 1
        return result