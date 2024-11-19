from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count_dic = Counter(nums)
        return [num for num, count in count_dic.items() if count == 2]