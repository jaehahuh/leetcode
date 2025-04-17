class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = defaultdict(list)
        for i, n in enumerate(nums):
            pairs[n].append(i)
    
        count = 0
        for indices in pairs.values():
            length = len(indices)
            for i in range(length):
                for j in range(i + 1, length):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1
        return count