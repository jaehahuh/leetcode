class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result = 0
        left = 0
        count_dict = defaultdict(int)
        for right in range(len(s)):
            count_dict[s[right]] += 1
            while len(count_dict) == 3:
                result += len(s) - right
                count_dict[s[left]] -= 1
                if count_dict[s[left]] == 0:
                    del count_dict[s[left]]
                left += 1

        return result