class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def prime_num(num:int) -> bool:
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        count = 0
        for num in range(left, right+1):
            binary_num = bin(num)
            num_bits = binary_num.count('1')
            if prime_num(num_bits):
                count += 1

        return count