class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # 0~32 범위에 대해 소수 여부 미리 계산
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

        count = 0
        for num in range(left, right + 1):
            ones = num.bit_count()
            if ones in prime_set:
                count += 1

        return count