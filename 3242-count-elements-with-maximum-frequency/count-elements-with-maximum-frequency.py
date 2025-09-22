class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count_dict = Counter(nums)
        max_freq = max(count_dict.values())
        count_max = sum(1 for value in count_dict.values() if value == max_freq)
        return count_max * max_freq