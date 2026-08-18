class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counts = Counter(nums)

        if k == 1:
            valid = [num for num, cnt in counts.items() if cnt == 1]
            return max(valid) if valid else -1
        
        if k == n:
            return max(nums)
        
        result = -1
        if counts[nums[0]] == 1:
            result = max(result, nums[0])
        if counts[nums[-1]] == 1:
            result = max(result, nums[-1])
            
        return result
            
            
            