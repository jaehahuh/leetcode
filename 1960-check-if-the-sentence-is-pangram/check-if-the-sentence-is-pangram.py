class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        
        count_dict = {}
        for ch_code in range(ord('a'), ord('z') + 1):
            alpha = chr(ch_code)
            count_dict[alpha] = 0
        
        for ch in sentence:
            count_dict[ch] += 1
        
        return all(count > 0 for count in count_dict.values())