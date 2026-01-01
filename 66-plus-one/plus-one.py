class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(str(num) for num in digits)
        s_num = str(int(s) + 1)
        new_digits = list(s_num)
        return [int(ch) for ch in new_digits] 