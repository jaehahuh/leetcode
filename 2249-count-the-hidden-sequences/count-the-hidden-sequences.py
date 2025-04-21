class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix_sum = [0]
        for diff in differences:
            prefix_sum.append(prefix_sum[-1] + diff)
    
        min_prefix = min(prefix_sum)
        max_prefix = max(prefix_sum)
    
        start = lower - min_prefix
        end = upper - max_prefix

        count = max(0, end - start + 1)
        return count