class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        last = [-1] * m
        
        idx1 = n - 1
        for j in range(m - 1, -1, -1):
            while idx1 >= 0 and word1[idx1] != word2[j]:
                idx1 -= 1
            if idx1 < 0:
                break
            last[j] = idx1
            idx1 -= 1

        ans = []
        changed = False
        i = 0
        
        for j in range(m):
            while i < n:
                is_match = (word1[i] == word2[j])
                can_change = (not changed) and (j == m - 1 or last[j + 1] > i)
                
                if is_match or can_change:
                    if not is_match:
                        changed = True
                    ans.append(i)
                    i += 1
                    break
                
                i += 1
            
            if len(ans) <= j:
                return []
                
        return ans