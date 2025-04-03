class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_i = [0] * n
        max_k = [0] * n

        # Calculate max_i array (maintain maximum from the left)
        max_i[0] = nums[0]
        for i in range(n):
            max_i[i] = max(max_i[i - 1], nums[i])

        # Calculate max_k array (maintain maximum from the right)
        max_k[n-1] = nums[n-1]
        for k in range(n - 2, -1, -1):
            max_k[k] = max(max_k[k + 1] , nums[k])

        max_value = 0
        for j in range(1, n-1):
            value_of_triplet = (max_i[j - 1] - nums[j]) * max_k[j + 1]
            max_value = max(max_value, value_of_triplet)

        return max_value 