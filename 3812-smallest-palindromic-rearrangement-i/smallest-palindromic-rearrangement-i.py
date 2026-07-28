class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count_dict = Counter(s)
        if len(count_dict) == 1:
            return s
        
        half = []
        mid = ''
        ch_list = sorted(count_dict.keys())
        for c in ch_list:
            if count_dict[c] % 2 != 0:
                mid = c
            half.append(c * (count_dict[c] // 2))
        
        left_half = ''.join(half)
        right_half = left_half[::-1]
        return left_half + mid + right_half