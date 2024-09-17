class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_words = s1.split()
        s2_words = s2.split()
        total = s1_words + s2_words
        total_count = collections.Counter(total)
        return [word for word in total_count if total_count[word] == 1]