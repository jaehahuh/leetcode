class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        result = []
        lst = sentence.split(' ')
        a_count = 1
        for word in lst:
            if word[0] in 'aeiouAEIOU':
                result.append(word[:] + 'ma' + 'a' * a_count)
                a_count += 1
            else:
                result.append(word[1:] + word[0] + 'ma' + 'a' * a_count)
                a_count += 1  
                  
        return ' '.join(result)