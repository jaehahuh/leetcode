class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs = 0
        count = defaultdict(int)
    
        for a, b in dominoes:
            key = tuple(sorted((a,b)))
            pairs += count[key]
            count[key] += 1
            
        return pairs