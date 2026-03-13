class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def canFinish(t):
            total_height = 0

            for w in workerTimes:
                val = (2 * t) // w
                x = (math.isqrt(1 + 4 * val) - 1) // 2

                total_height += x
                if total_height >= mountainHeight:
                    return True
            
            return False
        
        left, right = 0, 10 ** 16
        result = right

        while left <= right:
            mid = (left + right) // 2
            if canFinish(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result