class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        window_start = 0
        consec_count = 1

        for window_end in range(len(nums)):
            if window_end > 0 and nums[window_end - 1] + 1 == nums[window_end]:
                consec_count += 1

            if window_end - window_start + 1 > k:
                if nums[window_start] + 1 == nums[window_start + 1]:
                    consec_count -= 1
                window_start += 1
                
            if window_end - window_start + 1 == k:
                res.append(nums[window_end] if consec_count == k else -1)
    
        return res