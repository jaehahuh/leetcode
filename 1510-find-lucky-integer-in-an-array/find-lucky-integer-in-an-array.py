class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky_integer = -1

        num_dict = Counter(arr)
        for num in num_dict:
            if num == num_dict[num] and num > lucky_integer:
                lucky_integer = num
        
        return lucky_integer