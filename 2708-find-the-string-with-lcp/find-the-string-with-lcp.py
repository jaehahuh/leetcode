class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        words = [None] * n
        next_alpha = ord('a')

        for i in range(n):
            if words[i] is not None:
                continue

            if next_alpha > ord('z'):
                return ''

            curr_char = chr(next_alpha)
            if lcp[i][i] == 0: 
                return ""
                
            for j in range(i, n):
                if lcp[i][j] > 0:
                    words[j] = curr_char

            next_alpha += 1

        result_word = ''.join(words) 

        # Validation
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if result_word[i] == result_word[j]:
                    if i == n - 1 or j == n - 1:
                        lcp_value = 1
                    else:
                        lcp_value = 1 + lcp[i + 1][j + 1]
                else:
                    lcp_value = 0

                if lcp[i][j] != lcp_value:
                    return ""
        
        return result_word