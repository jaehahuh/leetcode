class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1 
        self.nums2 = nums2
        self.nums2_counts = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.nums2_counts[old_val] -= 1
        self.nums2[index] += val
        new_val = self.nums2[index]
        self.nums2_counts[new_val] += 1

    def count(self, tot: int) -> int:
        total_pairs = 0
        for num1 in self.nums1:
            target_num2 = tot - num1
            total_pairs += self.nums2_counts.get(target_num2, 0)

        return total_pairs
        
# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)