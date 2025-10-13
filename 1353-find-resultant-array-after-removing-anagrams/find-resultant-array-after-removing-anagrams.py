class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            if result and sorted(result[-1]) == sorted(word):
                continue
            else:
                result.append(word)

        return result