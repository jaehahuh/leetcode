class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        min_delete = float('inf')
        word_freq = Counter(word)
        sorted_freq = sorted(word_freq.values())
        
        for i in range(len(sorted_freq)):
            target = sorted_freq[i]
            delete = 0

            for left in range(i): #left side : deleted all small freqs
                delete += sorted_freq[left] 

            for right in range(i+1, len(sorted_freq)): #right side : Delete only excess freqs
                if sorted_freq[right] > target + k:
                    delete +=  sorted_freq[right] - (target + k)
            
            min_delete = min(min_delete, delete)
        return min_delete