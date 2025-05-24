class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i in range(len(words)):
            for ch in words[i]:
                if ch == x:
                    result.append(i)
                    break
        return result