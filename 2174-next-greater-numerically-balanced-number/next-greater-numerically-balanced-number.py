class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def check_balance(num):
            str_n = str(num)
            count = Counter(str_n)
            if '0' in count:
                return False
            for ch, count in count.items():
                if int(ch) != count:
                    return False
            return True
            
        new_num = n + 1
        while True:
            if check_balance(new_num):
                return new_num
            new_num += 1