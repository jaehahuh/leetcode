class Solution:
    def minimumSum(self, num: int) -> int:
        sorted_lst = sorted(str(num))
        new1 = int(sorted_lst[0])*10 + int(sorted_lst[2])
        new2 = int(sorted_lst[1])*10 + int(sorted_lst[3])
        return new1 + new2