class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        dp = [0] * (n+1)
        prefix_sum = [0] * (n+2)

        dp[0] = 1
        prefix_sum[1] = dp[0]

        min_deque = collections.deque()
        max_deque = collections.deque()

        left = 0
        for i in range(1, n+1):
            while min_deque and nums[min_deque[-1]] >= nums[i-1]:
                min_deque.pop()
            min_deque.append(i-1) 

            while max_deque and nums[max_deque[-1]] <= nums[i-1]:
                max_deque.pop()
            max_deque.append(i-1)

            while nums[max_deque[0]] - nums[min_deque[0]] > k:
                left += 1 
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()
            
            dp[i] = (prefix_sum[i] - prefix_sum[left] + MOD) % MOD
            prefix_sum[i+1] = (prefix_sum[i] + dp[i]) % MOD
        return dp[n]