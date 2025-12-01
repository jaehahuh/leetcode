class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def check(time):
            current_time = 0
            for power in batteries:
                current_time += min(power, time)
            return current_time >= n * time

        result = 0
        low = 0
        high = (sum(batteries)//n) + 1
        while low <= high:
            mid = low + (high - low) // 2
            if mid == 0:
                low = mid + 1
                continue
            
            if check(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result