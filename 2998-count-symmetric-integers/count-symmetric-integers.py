class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high+1):
            str_num = str(num)
            if len(str_num)%2 == 0:
                mid = len(str_num)//2
                first_digits = str_num[:mid]
                last_digits = str_num[mid:]
                first_sum = sum(int(digit) for digit in first_digits)
                last_sum = sum(int(digit) for digit in last_digits)
                if first_sum == last_sum:
                    count += 1
        return count