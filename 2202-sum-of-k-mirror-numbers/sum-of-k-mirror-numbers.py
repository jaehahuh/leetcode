class Solution:
    def kMirror(self, k: int, n: int) -> int:
        total_sum = 0
        count = 0

        def is_mirror_str(s):
            return s == s[::-1]

        def convert_base(num, k):
            base_digits = []
            while num > 0:
                base_digits.append(str(num % k))
                num //= k
            return ''.join(reversed(base_digits)) if base_digits else '0'

        def generate_mirror_numbers():
            # Single-digit palindromes
            for i in range(1, 10):
                yield i

            length = 1
            while True:
                # Even-length palindromes
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    mirror = int(s + s[::-1])
                    yield mirror
                # Odd-length palindromes
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    for mid in '0123456789':
                        mirror = int(s + mid + s[::-1])
                        yield mirror
                length += 1

        for number_10 in generate_mirror_numbers():
            number_k = convert_base(number_10, k)
            if is_mirror_str(number_k):
                total_sum += number_10
                count += 1
                if count == n:
                    break

        return total_sum