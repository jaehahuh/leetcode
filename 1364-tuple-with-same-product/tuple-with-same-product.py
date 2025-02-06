class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int) #num1 * num2 => count
        pair_count = defaultdict(int) #num1 * num2 => count of pair  (a * b), (c * d)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                pair_count[product] += product_count[product]
                product_count[product] += 1

        result = 0
        for count in pair_count.values():
                result += count * 8
        
        return result