class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        bit_size = 2 * n + 3
        bit = [0] * bit_size

        def update(index, value):
            while index < bit_size:
                bit[index] += value
                index += index & (-index)
        
        def query(index):
            total = 0
            while index > 0:
                total += bit[index]
                index -= index & (-index)
            return total
        
        result = 0
        curr_sum = 0

        offset = n + 2
        update(curr_sum + offset, 1)

        for num in nums:
            if num == target:
                curr_sum += 1
            else:
                curr_sum -= 1
        
            result += query(curr_sum + offset - 1)
            update(curr_sum + offset, 1)
        
        return result