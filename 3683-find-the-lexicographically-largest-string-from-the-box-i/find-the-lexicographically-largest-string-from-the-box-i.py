class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # Edge case: if only one friend, the whole word is the only valid split
        if numFriends == 1:
            return word
        
        # Find the lexicographically largest suffix
        max_suffix = self.findLastLexSubstring(word)
        
        # We can only use up to (len(word) - numFriends + 1) characters
        max_length = len(word) - numFriends + 1
        
        return max_suffix[:max_length]

    # Function to find the lexicographically largest suffix in O(n) time
    def findLastLexSubstring(self, s: str) -> str:
        start = 0
        candidate = 1
        offset = 0

        while candidate + offset < len(s):
            if s[start + offset] == s[candidate + offset]:
                offset += 1
            elif s[start + offset] > s[candidate + offset]:
                # Current suffix is better; skip candidate range
                candidate = candidate + offset + 1
                offset = 0
            else:
                # Found a better candidate suffix
                start = max(start + offset + 1, candidate)
                candidate = start + 1
                offset = 0

        return s[start:]