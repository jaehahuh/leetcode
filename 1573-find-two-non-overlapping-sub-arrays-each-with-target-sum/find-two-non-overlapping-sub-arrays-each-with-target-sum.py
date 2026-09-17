class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        min_lens = [float('inf')] * n

        prefix_map = {0: -1}
        curr_sum = 0
        result = float('inf')
        min_len = float('inf')

        for i in range(n):
            curr_sum += arr[i]
            target_sum = curr_sum - target

            if target_sum in prefix_map:
                start_index = prefix_map[target_sum]
                curr_len = i - start_index

                if start_index >= 0 and min_lens[start_index] != float('inf'):
                    result = min(result, curr_len + min_lens[start_index])
                
                min_len = min(min_len, curr_len)

            min_lens[i] = min_len
            prefix_map[curr_sum] = i

        return result if result != float('inf') else -1