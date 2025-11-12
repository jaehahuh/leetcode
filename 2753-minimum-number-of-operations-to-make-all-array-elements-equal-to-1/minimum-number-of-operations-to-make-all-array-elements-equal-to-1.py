class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a   
        
        n = len(nums)
        count_ones = nums.count(1)
        if count_ones > 0:
            return n - count_ones
        
        check_gcd = 0
        for num in nums:
            check_gcd = gcd(check_gcd, num)
        
        if check_gcd != 1: # Impossible to make all elements equal to 1.
            return -1
        
        min_ops_to_create_one = float('inf')

        for i in range(n):
            current_gcd_in_subarray = nums[i]
            for j in range(i+1, n):
                current_gcd_in_subarray = gcd(current_gcd_in_subarray, nums[j])
                if current_gcd_in_subarray == 1:
                    min_ops_to_create_one = min(min_ops_to_create_one, j - i)
                    break
        
        return min_ops_to_create_one + (n - 1)