class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        min_land_end = min(landStartTime[i] + landDuration[i] for i in range(n))
        min_water_end = min(waterStartTime[j] + waterDuration[j] for j in range(m))

        best_land_first = min(max(min_land_end, waterStartTime[j]) + waterDuration[j] for j in range(m))
        best_water_first = min(max(min_water_end, landStartTime[i]) + landDuration[i] for i in range(n))

        return min(best_land_first, best_water_first)