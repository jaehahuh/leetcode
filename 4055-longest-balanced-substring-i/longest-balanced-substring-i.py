class Solution:
    def longestBalanced(self, s: str) -> int:
        def check_all_values_same(dict) -> bool:
            values = dict.values()
            return len(set(values)) == 1

        n = len(s)
        max_sub_length = 0

        for start in range(n):
            count_dict = defaultdict(int)
            for end in range(start, n):
                count_dict[s[end]] += 1
                if check_all_values_same(count_dict):
                    sub_length = end - start + 1
                    if sub_length > max_sub_length:
                        max_sub_length = sub_length
        
        return max_sub_length