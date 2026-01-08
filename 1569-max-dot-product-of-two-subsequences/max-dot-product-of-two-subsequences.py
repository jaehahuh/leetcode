class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                curr_product = nums1[i-1] * nums2[j-1]
                take_curr_pair = curr_product + max(0, dp[i-1][j-1])
                skip_num1 = dp[i-1][j]
                skip_num2 = dp[i][j-1]
                dp[i][j] = max(take_curr_pair, skip_num1, skip_num2)
        
        return dp[m][n]