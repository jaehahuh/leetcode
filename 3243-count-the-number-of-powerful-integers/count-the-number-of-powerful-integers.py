from functools import lru_cache

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        m = len(s)

        # Build KMP-style transition table
        next_kmp = [[0] * 10 for _ in range(m + 1)]
        for k in range(m + 1):
            for d in range(10):
                t = s[:k] + str(d)
                for l in range(min(len(t), m), -1, -1):
                    if t.endswith(s[:l]):
                        next_kmp[k][d] = l
                        break

        def count_up_to(bound: int) -> int:
            S = str(bound)
            n = len(S)

            @lru_cache(maxsize=None)
            def dp(pos: int, tight: bool, leading_zero: bool, k: int) -> int:
                if pos == n:
                    return int(k == m)

                res = 0
                max_digit = int(S[pos]) if tight else 9

                for d in range(0, max_digit + 1):
                    # Enforce digit limit condition always
                    if d > limit:
                        continue

                    new_tight = tight and (d == max_digit)
                    new_leading_zero = leading_zero and (d == 0)
                    new_k = 0 if new_leading_zero else next_kmp[k][d]

                    res += dp(pos + 1, new_tight, new_leading_zero, new_k)

                return res
            return dp(0, True, True, 0)
            
        return count_up_to(finish) - count_up_to(start - 1)