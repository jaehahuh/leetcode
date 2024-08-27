import collections

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic = collections.Counter(arr)
        count = 0
        for s in arr:
            if dic[s] == 1:
                count += 1
                if count == k:
                    return s 
        return ""