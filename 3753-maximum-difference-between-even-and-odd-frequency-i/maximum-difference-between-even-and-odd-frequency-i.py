class Solution:
    def maxDifference(self, s: str) -> int:
        sorted_s = sorted(s)
        odd_lst = []
        even_lst = []
        count = 1
        word = sorted_s[0]
        for i in range(1,len(sorted_s)):
            if sorted_s[i-1] == sorted_s[i]:
                word += sorted_s[i]
                count += 1
            else:
                if count % 2 == 0:
                    even_lst.append(word)
                    word = sorted_s[i]
                    count = 1
                else:
                    odd_lst.append(word)
                    word = sorted_s[i]
                    count = 1

        if count % 2 == 0:
            even_lst.append(word)
        else:
            odd_lst.append(word)

        odd_lst.sort(key=len)
        even_lst.sort(key=len)

        max_odd = len(odd_lst[-1])
        least_even = len(even_lst[0])

        max_diff = max_odd - least_even
        return max_diff