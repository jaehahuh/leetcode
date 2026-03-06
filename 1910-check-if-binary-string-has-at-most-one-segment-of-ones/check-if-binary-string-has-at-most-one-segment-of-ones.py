class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        last_one_index = 0 

        if n == 1:
            return True
       
        for i in range(1, n):
            if s[i] == '0':
                last_one_index = i
                break
            last_one_index = i
        
        if n == last_one_index+1:
            return True
        
        for i in range(last_one_index, n):
            if s[i] == '1':
                return False
        
        return True