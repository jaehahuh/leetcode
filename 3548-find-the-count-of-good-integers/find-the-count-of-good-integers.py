from collections import Counter
from math import factorial
from functools import lru_cache

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        @lru_cache(None)
        def fact(x):
            return factorial(x)

        def count_permutations(counter):
            total = sum(counter.values())
            res = fact(total)
            for val in counter.values():
                res //= fact(val)
            if '0' in counter:
                counter0 = counter.copy()
                counter0['0'] -= 1
                if counter0['0'] == 0:
                    del counter0['0']
                total0 = total - 1
                res0 = fact(total0)
                for val in counter0.values():
                    res0 //= fact(val)
                res -= res0
            return res

        def build_palindromes(n):
            res = []
            half = (n + 1) // 2
            start = 10 ** (half - 1)
            end = 10 ** half
            for first_half in range(start, end):
                s = str(first_half)
                if n % 2 == 0:
                    full = s + s[::-1]
                else:
                    full = s + s[:-1][::-1]
                num = int(full)
                if num % k == 0:
                    res.append(Counter(full))
            return res

        seen = set()
        for c in build_palindromes(n):
            seen.add(tuple(sorted(c.items())))

        ans = 0
        for tup in seen:
            counter = Counter(dict(tup))
            ans += count_permutations(counter)

        return ans
