class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        index_map = {num : i+1 for i, num in enumerate(sorted_arr)}
        return [index_map[num] for num in arr]