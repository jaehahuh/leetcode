class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float("-inf")
        i = 0

        while i < n:
            l = i
            i += 1

            # Find the first strictly increasing segment
            while i < n and nums[i - 1] < nums[i]:
                i += 1
            if i == l + 1:
                # No valid increasing segment found, move forward
                continue

            p = i - 1
            
            # Initialize sum with last two elements of increasing segment as start of decreasing segment
            s = nums[p - 1] + nums[p]

            # Find the second strictly decreasing segment and add sum
            while i < n and nums[i - 1] > nums[i]:
                s += nums[i]
                i += 1
            if i == p + 1 or i == n or (i < n and nums[i - 1] == nums[i]):
                # Invalid decreasing segment conditions, skip
                continue

            q = i - 1
            
            # Add the first element of the third segment (strictly increasing)
            s += nums[i]
            i += 1

            # Find the maximum sum suffix of the third strictly increasing segment
            max_suffix = 0
            curr_sum = 0
            while i < n and nums[i - 1] < nums[i]:
                curr_sum += nums[i]
                max_suffix = max(max_suffix, curr_sum)
                i += 1
            s += max_suffix

            # Find the maximum sum prefix of the first strictly increasing segment before p-1
            max_prefix = 0
            curr_sum = 0
            start = max(l, 0)
            end = max(p - 2, l)
            for j in range(p - 2, start - 1, -1):
                curr_sum += nums[j]
                max_prefix = max(max_prefix, curr_sum)
            s += max_prefix

            # Update the answer and reset pointer to continue searching
            ans = max(ans, s)
            i = q

        return ans