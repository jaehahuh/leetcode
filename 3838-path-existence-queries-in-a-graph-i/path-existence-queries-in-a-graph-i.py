class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        group_ids = [0] * n
        current_group = 0

        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                current_group += 1
            group_ids[i] = current_group
        
        result = []
        for u, v in queries:
            if group_ids[u] == group_ids[v]:
                result.append(True)
            else:
                result.append(False)
        
        return result