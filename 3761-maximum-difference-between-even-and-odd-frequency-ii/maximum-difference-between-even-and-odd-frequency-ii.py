class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def get_status(a: int, b: int) -> int:
            return ((a & 1) << 1) | (b & 1)

        n = len(s)
        ans = float('-inf')

        for ca in range(5):         # 문자 a 후보 (0~4)
            for cb in range(5):     # 문자 b 후보 (0~4)
                if ca == cb:
                    continue
                best = [float('inf')] * 4
                cnt_a = cnt_b = prev_a = prev_b = 0
                left = -1
                for right in range(n):
                    if s[right] == str(ca):
                        cnt_a += 1
                    if s[right] == str(cb):
                        cnt_b += 1

                    while right - left >= k and cnt_b - prev_b >= 2:
                        st = get_status(prev_a, prev_b)
                        best[st] = min(best[st], prev_a - prev_b)
                        left += 1
                        if s[left] == str(ca):
                            prev_a += 1
                        if s[left] == str(cb):
                            prev_b += 1

                    st = get_status(cnt_a, cnt_b)
                    opp = st ^ 2  # a 홀수 & b 짝수 조건에 해당하는 status
                    if best[opp] != float('inf'):
                        ans = max(ans, cnt_a - cnt_b - best[opp])

        return ans
