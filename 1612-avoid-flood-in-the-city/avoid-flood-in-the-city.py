class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        result = [1] * len(rains)  # Default value for dry days
        last_rain = {}    # lake -> last day it rained on that lake
        dry_days = []    # Sorted list of indices where drying is possible (rains[i] == 0)

        for i, lake in enumerate(rains):
            if lake == 0:
                bisect.insort(dry_days, i)  # Store this day as an available drying slot
            else:
                result[i] = -1 # On raining days, must set -1
                if lake in last_rain:
                    # Find the earliest dry day after the last rain on this lake
                    prev = last_rain[lake]
                    pos = bisect.bisect_right(dry_days, prev)
                    if pos == len(dry_days):
                        # No available dry day to prevent flood
                        return []
                    dry_day = dry_days.pop(pos)
                    result[dry_day] = lake # Assign this dry day to dry the specific lake
                last_rain[lake] = i # Update the last raining day for this lake
        return result