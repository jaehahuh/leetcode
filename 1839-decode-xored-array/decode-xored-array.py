class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for i in range(len(encoded)):
            num = arr[-1] ^ encoded[i]
            arr.append(num)
        return arr