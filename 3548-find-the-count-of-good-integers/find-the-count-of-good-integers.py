from collections import Counter
from math import factorial
from functools import lru_cache

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        
        # 팩토리얼을 캐싱하여 빠르게 계산 (조합 계산용)
        @lru_cache(None)
        def fact(x):
            return factorial(x)

        # Counter를 통해 해당 자리수 조합으로 만들 수 있는 n자리 수의 개수를 계산
        def count_valid_permutations(counter: Counter) -> int:
            total_digits = sum(counter.values())
            total_perm = fact(total_digits)
            for freq in counter.values():
                total_perm //= fact(freq)

            # 앞자리가 0인 경우 제거
            if '0' in counter:
                counter_zero = counter.copy()
                counter_zero['0'] -= 1
                if counter_zero['0'] == 0:
                    del counter_zero['0']
                digits_excluding_zero = total_digits - 1
                invalid_perm = fact(digits_excluding_zero)
                for freq in counter_zero.values():
                    invalid_perm //= fact(freq)
                total_perm -= invalid_perm

            return total_perm

        # n자리 팰린드롬 숫자 중 k로 나누어떨어지는 수의 digit Counter를 생성
        def generate_k_palindrome_counters(n: int, k: int):
            valid_counters = []
            half_len = (n + 1) // 2  # 팰린드롬 앞쪽 절반만 생성
            start = 10 ** (half_len - 1)
            end = 10 ** half_len

            for first_half in range(start, end):
                s = str(first_half)
                # 짝수 vs 홀수 길이에 따라 팰린드롬 완성
                if n % 2 == 0:
                    full_palindrome = s + s[::-1]
                else:
                    full_palindrome = s + s[:-1][::-1]

                number = int(full_palindrome)
                if number % k == 0:
                    valid_counters.append(Counter(full_palindrome))

            return valid_counters

        # 1. k로 나눠지는 팰린드롬 수들의 자리수 Counter 모음
        k_palindrome_counters = generate_k_palindrome_counters(n, k)

        # 2. 중복 방지를 위해 Counter를 정렬된 튜플로 변환하여 set에 저장
        unique_digit_patterns = set()
        for counter in k_palindrome_counters:
            unique_digit_patterns.add(tuple(sorted(counter.items())))

        # 3. 각 패턴이 만들어낼 수 있는 n자리 수 조합의 개수를 더함
        total_good_integers = 0
        for pattern in unique_digit_patterns:
            counter = Counter(dict(pattern))
            total_good_integers += count_valid_permutations(counter)

        return total_good_integers