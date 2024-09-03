class Solution:
    def getLucky(self, s: str, k: int) -> int:
        #hash map for letters to num
        dic = {chr(ord("a") + i): str(i + 1) for i in range(26)}

        #Convert
        num_str = ''
        for ch in s:
            num_str += dic[ch]

        #Transform
        while k > 0:
            total = 0
            for n in num_str:
                total += int(n)
            num_str = str(total)
            k -= 1
        
        return total