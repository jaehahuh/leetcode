class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alpha_map = {}
        for i in range(26):
            alpha_map[i] = chr(ord('z') - i)
        
        weight_map = {} 
        for i in range(len(weights)):
            weight_map[chr(ord('a') + i)] = weights[i]
        
        result = ''
        for word in words:
            total = 0
            for ch in word:
                total += weight_map[ch]
            total = total % 26
            result += alpha_map[total]
        
        return result