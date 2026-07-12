class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        index_map = defaultdict(int)
        for i in range(len(sorted_arr)):
            index_map[sorted_arr[i]] = i+1
        
        result = []
        for num in arr:
            result.append(index_map[num])
        
        return result