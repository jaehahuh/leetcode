class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = []
        suffix = [0] * len(nums)
        seen_pre = set()
        seen_suf = set()

        #count distinct prefix
        for i in range(n):
            seen_pre.add(nums[i])
            prefix.append(len(seen_pre))
        
        #count distinct suffix
        for i in range(n-1, -1, -1):
            if i + 1 < n:
                suffix[i] = len(seen_suf)
            seen_suf.add(nums[i])
        
        diff_lst = []
        for i in range(n):
            diff = prefix[i] - suffix[i]
            diff_lst.append(diff)
        
        return diff_lst