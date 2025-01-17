class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        first = 0
        last = 0
        for bit in derived:
            if bit == 1:
                last = ~last

        return first == last