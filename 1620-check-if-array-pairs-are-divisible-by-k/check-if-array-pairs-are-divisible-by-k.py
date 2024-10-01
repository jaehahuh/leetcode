class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = [0] * k
        for num in arr:
            remainder = num % k
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1

        for i in range((k // 2) + 1):
            if i == 0:  # 나머지가 0인 경우
                if remainder_count[i] % 2 != 0:
                    return False
            elif i == k - i:  # 나머지가 k/2인 경우 (k가 짝수일 때)
                if remainder_count[i] % 2 != 0:
                    return False
            else:
                if remainder_count[i] != remainder_count[k - i]:
                    return False
        return True