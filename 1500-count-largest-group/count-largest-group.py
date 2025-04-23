class Solution:
    def countLargestGroup(self, n: int) -> int:
        max_digit_sum = 9 * len(str(n))  # maximum digit sum
        count_dict = {n:0 for n in range(1, max_digit_sum+1)}

        for num in range(1, n+1):
            digits = list(str(num))
            digits_sum = sum(int(d) for d in digits)
            count_dict[digits_sum] += 1

        max_value = max(count_dict.values())
        result = sum(1 for value in count_dict.values() if value == max_value)

        return result 