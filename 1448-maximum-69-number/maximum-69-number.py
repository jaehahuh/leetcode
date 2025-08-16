class Solution:
    def maximum69Number (self, num: int) -> int:
        result = []
        count = 1
        for n in str(num):
            if n == '6' and count == 1:
                result.append('9')
                count -= 1
            else:
                result.append(n)

        return int(''.join(result))