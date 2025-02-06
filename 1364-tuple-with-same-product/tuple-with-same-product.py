class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int) #num1 * num2 => count

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                product_count[product] += 1

        result = 0
        for count in product_count.values():
                pairs = (count * (count - 1 )//2)
                result += pairs * 8
        
        return result

        # 1 count -> 0 pair -> 0 tuples
        # 2 count -> 1 pair -> 8 tuples
        # 3 count -> 3 pair -> 24 tuples
        # 4 count -> 6 pair -> 48 tuples
        # 5 count -> 10 pair -> 80 tuples