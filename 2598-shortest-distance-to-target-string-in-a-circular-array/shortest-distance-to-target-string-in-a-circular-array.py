class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = n

        for i, word in enumerate(words):
            if word == target:
                dist = abs(startIndex - i)
                min_dist = min(min_dist, dist, n-dist)
        
        return min_dist if min_dist != n else -1