class Solution:
    def hasSameDigits(self, s: str) -> bool:
        current_s = s
        while len(current_s) > 2:
            digit_lst = []
            for i in range(1, len(current_s)):
                new_digit = str((int(current_s[i-1]) + int(current_s[i])) % 10)
                digit_lst.append(new_digit)
            current_s = ''.join(digit_lst)
            
        return current_s[0] == current_s[1]