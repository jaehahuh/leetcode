class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for q in queries:
            for d in dictionary:
                diff = 0
                for ch_q, ch_d in zip(q, d):
                    if ch_q != ch_d:
                        diff += 1
                    if diff > 2:
                        break
                else: # if diff <= 2
                    result.append(q)
                    break
        
        return result