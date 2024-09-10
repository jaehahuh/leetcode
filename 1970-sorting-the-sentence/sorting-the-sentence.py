class Solution:
    def sortSentence(self, s: str) -> str:
        dic = {}
        lst = s.split(" ")
        count = 0  #count number of words in sentence
        for word in lst:
            dic[int(word[-1])] = word[:-1]
            count += 1

        result = ''
        for i in range(1,count+1):
            if i == count:
                result += dic[i]
            else:
                result += dic[i] + ' '
        
        return result