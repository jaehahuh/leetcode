class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        
        for ch in s:
            if ch != '9': 
                max_val = int(s.replace(ch, '9'))
                break
            else:
                max_val = num # if all digits are 9

        for ch in s:
            if ch != '0':
                min_val = int(s.replace(ch, '0'))
                break
            else:
                min_val = num
  
        return max_val - min_val