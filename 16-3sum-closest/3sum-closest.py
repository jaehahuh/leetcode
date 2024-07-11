class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        cloest = math.inf
        
        #make 3 pointers
        for i, num in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = num + nums[left] + nums[right]

                if target == total:
                    return total

                elif target < total:
                    right -= 1
                    if abs(target - total) < abs(target - cloest):
                        cloest = total

                else:
                    left += 1
                    if abs(target - total) < abs(target - cloest):
                        cloest = total
    
        return cloest