class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_set = set()
        count = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] not in nums_set:
                nums_set.add(nums[i])
                count += 1
            else:
                break

        remain_length = len(nums) - count
        remainder = remain_length % 3
        min_operation = (remain_length//3) if remainder == 0 else (remain_length//3) + 1
        return min_operation