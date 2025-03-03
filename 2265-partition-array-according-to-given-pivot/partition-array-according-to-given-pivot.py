class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivot_array = []
        less_array = []
        greater_array = []
        for num in nums:
            if num == pivot:
                pivot_array.append(num)
            elif num < pivot:
                less_array.append(num)
            else:
                greater_array.append(num)
        
        return less_array + pivot_array + greater_array