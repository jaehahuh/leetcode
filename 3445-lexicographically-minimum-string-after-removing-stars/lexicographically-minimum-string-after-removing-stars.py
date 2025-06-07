class Solution:
    def clearStars(self, s: str) -> str:
        char_indices = defaultdict(list)
        remove = [False] * len(s)

        for i, ch in enumerate(s):
            if ch == "*":
                remove[i] = True
                for i in range(ord('a'), ord('z') + 1):
                    char = chr(i)
                    if char_indices[char]:
                        remove[char_indices[char].pop()] = True
                        break
            else:
                char_indices[ch].append(i)
            
        return ''.join(s[i] for i in range(len(s)) if not remove[i])