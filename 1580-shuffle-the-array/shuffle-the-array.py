class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst1 = nums[:n]
        lst2 = nums[n:]
        output = []
        #since nums array length is 2n, lst1 and lst2 lengths are same
        for i in range(len(lst1)):
            output.append(lst1[i])
            output.append(lst2[i])
        return output