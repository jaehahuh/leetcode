class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        know = [set(lang) for lang in languages]

        # Collect users who are part of at least one friendship without a common language
        candidates = set()
        for u, v in friendships:
            u -= 1
            v -= 1  # Convert to 0-based indices
            if know[u].isdisjoint(know[v]):
                candidates.add(u)
                candidates.add(v)
        
        # If every friendship can already communicate, no teaching is required
        if not candidates:
            return 0
        
        count = [0] * (n+1)
        for user in candidates:
            for lang in know[user]:
                count[lang] += 1
        
        max_already_know = max(count)
        min_teaches = len(candidates) - max_already_know
        return min_teaches
        