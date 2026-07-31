class Solution:
    def minimumPushes(self, word: str) -> int:
        word_counts = Counter(word)
        sorted_counts = sorted(word_counts.values(), reverse=True)
        result = 0
        for i, count in enumerate(sorted_counts):
            pushes = (i//8) + 1
            result += pushes * count
        return result