class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # 이항 계수 (Combination)를 미리 계산
        # comb[i][j] = iCj
        comb = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        # 모듈러 거듭제곱 함수
        def mod_pow(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res

        # 재귀 + 메모이제이션을 사용한 DP 함수
        @lru_cache(None)
        def dp(remaining_m, remaining_k, index, carry):
            # 기본 케이스
            # 모든 nums 인덱스를 다 사용했을 때
            if index == n:
                # remaining_m이 0이고, 마지막 carry에서 필요한 1의 개수와 남은 k가 일치해야 됌
                final_set_bits = 0
                temp_carry = carry
                while temp_carry > 0:
                    final_set_bits += temp_carry % 2
                    temp_carry //= 2
                
                if remaining_m == 0 and remaining_k == final_set_bits:
                    return 1
                return 0

            if remaining_k < 0:
                return 0

            res = 0
            # 현재 nums[index]를 몇 번 사용할지 결정합니다 (count: 0부터 remaining_m까지)
            for count in range(remaining_m + 1):
                # 조합의 수: 남은 remaining_m 위치 중 count개를 선택하는 경우의 수
                combinations = comb[remaining_m][count]
                
                # nums[index]^count의 곱을 계산
                product_contribution = mod_pow(nums[index], count)
                
                # 다음 단계로 전달할 올림과 남은 k를 계산
                bit_val = (carry + count) % 2
                new_carry = (carry + count) // 2
                new_remaining_k = remaining_k - bit_val

                # 재귀 호출하여 결과를 누적
                sub_problem_res = dp(remaining_m - count, new_remaining_k, index + 1, new_carry)
                
                term = (combinations * product_contribution) % MOD
                term = (term * sub_problem_res) % MOD
                res = (res + term) % MOD

            return res

        return dp(m, k, 0, 0)