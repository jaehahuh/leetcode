class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        counts = Counter(digits)
        result = 0

        for num in range(100, 1000, 2):
            num_counts = Counter(int(d) for d in str(num))

            if all(counts[d] >= count for d, count in num_counts.items()):
                result += 1
        
        return result