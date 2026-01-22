class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0
        while len(nums) > 1:
            is_non_decreaing = True
            min_sum = float("inf")
            target_index = -1

            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i+1]
                if nums[i] > nums[i+1]:
                    is_non_decreaing = False
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    target_index = i

            if is_non_decreaing:
                break
            
            operations += 1
            nums[target_index] = min_sum
            nums.pop(target_index + 1)
        
        return operations