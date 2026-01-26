class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)

        result = []
        min_abs_diff = float('inf')
        
        for i in range(n-1):
            curr_num = arr[i]
            next_num = arr[i+1]
            diff = abs(curr_num - next_num)
            min_abs_diff = min(min_abs_diff, diff)
    
        for i in range(n-1):
            curr_num = arr[i]
            next_num = arr[i+1]
            diff = abs(curr_num - next_num)
            if min_abs_diff == diff:
                result.append([arr[i], arr[i+1]])
        
        return result