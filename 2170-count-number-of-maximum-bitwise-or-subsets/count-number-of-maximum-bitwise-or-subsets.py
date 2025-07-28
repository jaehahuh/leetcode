class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        n = len(nums)
        self.count = 0
        def dfs(index, current_or_sum):
            if index == n:
                if current_or_sum == max_or:
                    self.count += 1
                return

            dfs(index + 1, current_or_sum | nums[index])
            dfs(index + 1, current_or_sum)

        dfs(0, 0)
        return self.count