class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        count = 0
        char_dict = Counter(s)
        for num in char_dict.values():
            if num % 2 == 1:
                count += 1
        
        return True if count <= k else False