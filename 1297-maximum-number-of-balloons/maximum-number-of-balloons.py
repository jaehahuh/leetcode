class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_dict = Counter(text)
        b_count = count_dict.get('b', 0)
        a_count = count_dict.get('a', 0)
        l_count = count_dict.get('l', 0) // 2
        o_count = count_dict.get('o', 0) // 2
        n_count = count_dict.get('n', 0)
        return min(b_count, a_count, l_count, o_count, n_count)