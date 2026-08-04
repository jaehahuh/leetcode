class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = []
        smallest, largest = min(nums), max(nums)
        num_set = set(nums)
        for num in range(smallest, largest+1):
            if num not in num_set:
                result.append(num)
        return result