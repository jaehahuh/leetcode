class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        b1, m1, b2, m2 = 100003, 1000000007, 100019, 1000000009

        p1 = p2 = h1 = h2 = 1
        pw1, pw2, pr1, pr2 = [1] * (n + 1), [1] * (n + 1), [0] * (n + 1), [0] * (n + 1)
        h1 = h2 = 0

        for i, x in enumerate(nums):
            p1 = p1 * b1 % m1
            p2 = p2 * b2 % m2
            pw1[i + 1], pw2[i + 1] = p1, p2
            h1 = (h1 * b1 + x) % m1
            h2 = (h2 * b2 + x) % m2
            pr1[i + 1], pr2[i + 1] = h1, h2

        def check(k: int) -> bool:
            cnt = Counter(
                (
                    (pr1[i + k] - pr1[i] * pw1[k]) % m1,
                    (pr2[i + k] - pr2[i] * pw2[k]) % m2,
                )
                for i in range(n - k + 1)
            )
            return 1 in cnt.values()

        lo, hi, ans = 1, n, n
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans, hi = mid, mid - 1
            else:
                lo = mid + 1
        return ans