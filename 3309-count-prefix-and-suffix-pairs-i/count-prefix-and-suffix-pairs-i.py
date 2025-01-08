class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(word1, word2):
            if word1 == word2[:len(word1)] and word1 == word2[len(word2)-len(word1):]:
                print(word1, word2)
                return True
            else:
                return False

        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                flag = isPrefixAndSuffix(words[i], words[j])
                if flag == True:
                    count += 1
        
        return count