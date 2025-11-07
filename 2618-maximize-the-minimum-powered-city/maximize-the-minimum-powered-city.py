class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        n = len(stations)   
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + stations[i]
        
        def get_range_sum(index):
            left_bound = max(0, index - r)
            right_bound = min(n - 1, index + r)
            return prefix_sum[right_bound + 1] - prefix_sum[left_bound]

        def check(target_min_power):
            diff = [0] * (n + 1) 
            curr_k_needed = 0
            curr_power_from_added_stations = 0

            for i in range(n):
                curr_power_from_added_stations += diff[i] 
                
                curr_city_power = get_range_sum(i) + curr_power_from_added_stations
            
                if curr_city_power < target_min_power:
                    needed = target_min_power - curr_city_power
                    curr_k_needed += needed
                
                    if curr_k_needed > k:
                        return False
                    
                    curr_power_from_added_stations += needed 

                    end_idx_for_impact = i + 2 * r 
                    if end_idx_for_impact + 1 < n:
                        diff[end_idx_for_impact + 1] -= needed

            return True

        high = 2 * (10 ** 10) 
        low = 0
        result = 0 

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                result = mid    
                low = mid + 1   
            else:
                high = mid - 1  
        
        return result