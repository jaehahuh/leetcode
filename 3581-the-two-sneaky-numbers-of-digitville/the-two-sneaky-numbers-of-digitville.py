class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        count_dict = Counter(nums)
        for key, items in count_dict.items():
            if items > 1:
                result.append(key)
        return result