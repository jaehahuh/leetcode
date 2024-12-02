class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()  #a hash set to store the numbers we've seen
        for num in arr:
            if num * 2 in seen or (num//2 in seen and num%2 == 0):
                return True
            seen.add(num)
        return False