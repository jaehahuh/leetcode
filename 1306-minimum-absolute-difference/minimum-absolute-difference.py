class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)

        min_diff = float('inf')
        
        for i in range(n-1):
            curr_num = arr[i]
            next_num = arr[i+1]
            diff = next_num - curr_num

            if min_diff > diff:
                result = [[curr_num, next_num]]
                min_diff = diff
            elif min_diff == diff:
                result.append([curr_num, next_num])

        return result