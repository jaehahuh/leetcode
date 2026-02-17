class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count_bits(x):
            return bin(x).count('1')

        result = []
        for h in range(12):
            for m in range(60):
                if count_bits(h) + count_bits(m) == turnedOn:
                    result.append(f'{h}:{m:02d}')
            
        return result