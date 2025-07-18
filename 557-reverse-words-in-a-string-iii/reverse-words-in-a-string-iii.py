class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(' ')
        reversed_lst = [word[::-1] for word in lst]
        return ' '.join(reversed_lst)