class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_unique = len(set(nums))
        complete_count = 0

        for left in range(len(nums)):
            freq = defaultdict(int)
            unique = 0

            for right in range(left, len(nums)):
                num = nums[right]
                if freq[num] == 0:
                    unique += 1
                freq[num] += 1

                if unique == total_unique:
                # when it reach the required number of distinct elements, all subarrays extending to the right will also be complete
                    complete_count += len(nums) - right
                    break
        
        return complete_count