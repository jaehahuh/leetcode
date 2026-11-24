class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def prime_mask(x: int) -> int:
            primes = (2, 3, 5, 7)
            mask = 0
            for idx, p in enumerate(primes):
                if x % p == 0:
                    mask |= 1 << idx
            return mask

        masks = [prime_mask(x) for x in nums]
        left = 0
        cur_mask = 0
        # 두 원소로 이루어진 부분배열은 항상 prod == lcm * gcd를 만족하므로 기본값 2
        result = 2

        for right, m in enumerate(masks):
            while cur_mask & m:
                cur_mask ^= masks[left]
                left += 1

            cur_mask |= m
            result = max(result, right - left + 1)

        return result