class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count_dict = Counter(nums)
        longest_sub = 0

        for n in count_dict:
            if n + 1 in count_dict:
                curr_sub = count_dict[n] + count_dict[n+1]
                longest_sub = max(longest_sub, curr_sub)
                
        return longest_sub