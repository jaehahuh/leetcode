class Solution:
    def minimumLength(self, s: str) -> int:
        char_count = Counter(s)
        
        for char, count in char_count.items():
            while count > 2:
                count -= 2
            char_count[char] = count

        return sum(list(char_count.values()))