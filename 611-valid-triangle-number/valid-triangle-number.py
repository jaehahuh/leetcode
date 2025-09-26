class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        count = 0
        for k in range(n-1, -1, -1):
            if nums[k] == 0:
                continue
            i, j = 0, k-1
            while i < j:
                if nums[k] < nums[i] + nums[j]:
                    count += (j - i)
                    j -= 1 # Move j to consider a smaller second side while keeping k fixed
                else: 
                    i += 1 # If the sum is not large enough, increase it by moving i to the right
        return count