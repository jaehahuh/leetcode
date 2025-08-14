class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good_integer = '' 
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                curr_good_integer = num[i:i+3]
                if not max_good_integer or curr_good_integer > max_good_integer:
                    max_good_integer = curr_good_integer

        return max_good_integer