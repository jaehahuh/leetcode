class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_bit_num = max(nums)
        index_array = []
        for i, value in enumerate(nums):
            if value == max_bit_num:
                index_array.append(i)
        
        count = 1
        max_count = 1
        for i in range(1,len(index_array)):
            if (index_array[i-1] + 1) == index_array[i]:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 1

        max_count = max(count, max_count)
        return max_count