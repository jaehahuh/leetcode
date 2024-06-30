class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        lst = []
        for nums in digits:
            s += str(nums)
        
        num = int(s) + 1
        s_num = str(num)

        for ch in s_num:
            lst.append(int(ch))

        return lst