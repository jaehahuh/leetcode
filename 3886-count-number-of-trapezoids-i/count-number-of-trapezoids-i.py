class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        mod_inv_2 = pow(2, MOD - 2, MOD) # 2의 모듈러 역원 계산

        y_count = defaultdict(int)
        for x, y in points:
            y_count[y] += 1
        
        y_pair_comb_counts = []
        for count in y_count.values():
            if count >= 2:
                # C(n, 2) = n * (n - 1) / 2
                y_pair_comb_counts.append((count * (count - 1) // 2) % MOD)

        if not y_pair_comb_counts:
            return 0
        
        total_comb_sum = 0
        total_comb_square_sum = 0

        for comb_count in y_pair_comb_counts:
            total_comb_sum = (total_comb_sum + comb_count) % MOD
            total_comb_square_sum = (total_comb_square_sum + (comb_count * comb_count) % MOD) % MOD
        
        final_numerator = (total_comb_sum * total_comb_sum - total_comb_square_sum + MOD) % MOD
        trapezoid_count = (final_numerator * mod_inv_2) % MOD
        
        return trapezoid_count