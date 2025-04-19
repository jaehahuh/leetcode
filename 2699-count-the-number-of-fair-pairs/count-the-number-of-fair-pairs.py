class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        # Count pairs with sum less than or equal to boundary
        def countPairs(boundary):
            count = 0
            left, right = 0, len(nums)-1

            while left < right:
                if nums[left] + nums[right] <= boundary:
                    count += right - left # All pairs between left and right satisfy the condition
                    left += 1
                else:
                    right -= 1

            return count

        # (pairs with sum <= upper) - (pairs with sum <= lower-1) -----> sum of count between lower and upper
        return countPairs(upper) - countPairs(lower-1) 