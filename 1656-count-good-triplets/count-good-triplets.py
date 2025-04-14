class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(arr)
        prefix_count = [0] * 1001

        for j in range(n-1):
            for k in range(j+1, n):
                if abs(arr[j] - arr[k]) <= b:
                    right_boundary = min(arr[j] + a, arr[k] + c) 
                    left_boundary = max(arr[j] - a, arr[k] - c)

                    right_boundary = min(right_boundary, 1000)
                    left_boundary =  max(left_boundary , 0)

                    if left_boundary <= right_boundary:
                        count += prefix_count[right_boundary] - (0 if left_boundary == 0 else prefix_count[left_boundary-1])

            for index in range(arr[j], 1001):
                prefix_count[index] += 1
                
        return count