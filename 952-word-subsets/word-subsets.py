class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_count = Counter()
        
        for word2 in words2:
            word2_count = Counter(word2)
            for char, freq in word2_count.items():
                max_count[char] = max(max_count[char], freq)

        result = []
        for word1 in words1:
            word1_count = Counter(word1)
            flag = True
            for char, freq in max_count.items():
                if word1_count[char] < freq:
                    flag = False
                    break
            
            if flag:
                result.append(word1)
        
        return result