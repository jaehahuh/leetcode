class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        for word in words:
            total_weight = sum(weights[ord(char) - ord('a')] for char in word) % 26
            ch_map = chr(ord('z') - total_weight)
            result.append(ch_map)
        return ''.join(result)