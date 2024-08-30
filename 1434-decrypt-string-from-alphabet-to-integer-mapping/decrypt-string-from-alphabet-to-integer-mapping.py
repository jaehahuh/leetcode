class Solution:
    def freqAlphabets(self, s: str) -> str:
        #create a dictionary that maps numbers to letters
        alpha_dic = {}
        for n in range(26):
            alpha_dic[str(n+1)] = chr(ord('a')+n)

        result = ''
        i = 0
        while i < len(s):
            #handle case for 10# to 26#
            if i + 2 < len(s) and s[i+2] == '#':
                result += alpha_dic[s[i:i+2]]
                i += 3  # skip past number and '#'
            
            #handle case for 1 to 9
            else:
                result += alpha_dic[s[i]]
                i += 1            
        
        return result