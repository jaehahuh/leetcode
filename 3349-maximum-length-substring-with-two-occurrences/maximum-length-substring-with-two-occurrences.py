class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count_dict = defaultdict(int)
        left = 0
        max_length = 0

        for right in range(len(s)):
            count_dict[s[right]] += 1
            while count_dict[s[right]] > 2:
                count_dict[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length