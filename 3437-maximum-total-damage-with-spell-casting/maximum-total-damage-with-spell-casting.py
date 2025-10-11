class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        damage_counts = Counter(power)
        unique_powers = sorted(damage_counts.keys())
        n = len(unique_powers)

        dp = [0] * n

        damage_total_values = {p: p * damage_counts[p] for p in unique_powers}

        dp[0] = damage_total_values[unique_powers[0]]
        for i in range(1, n):
            current_power = unique_powers[i]
            current_total_val = damage_total_values[current_power]
            
            skip_current_power_damage = dp[i-1]
            take_current_power_damage = current_total_val

            insert_index = bisect.bisect_left(unique_powers, current_power - 2, 0, i)

            prev_eligible_index = insert_index - 1
            if prev_eligible_index >= 0:
                take_current_power_damage += dp[prev_eligible_index]
            
            dp[i] = max(skip_current_power_damage, take_current_power_damage)
            
        return dp[n-1]

