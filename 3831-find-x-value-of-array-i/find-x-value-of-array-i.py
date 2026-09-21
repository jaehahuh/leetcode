class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        prev_dp = {}

        for num in nums:
            curr_dp = {}
            val = num % k

            curr_dp[val] = curr_dp.get(val, 0) + 1

            for rem, count in prev_dp.items():
                new_rem = (rem * val) % k
                curr_dp[new_rem] = curr_dp.get(new_rem, 0) + count
            
            for rem, count in curr_dp.items():
                result[rem] += count
            
            prev_dp = curr_dp
        
        return result