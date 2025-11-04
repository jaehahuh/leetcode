class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n-k+1):
            count_nums = collections.defaultdict(int)
            for j in range(i, i+k):
                count_nums[nums[j]] += 1
            top_x_items = heapq.nlargest(x, count_nums.items(), key=lambda item: (item[1], item[0]))
            
            top_x_sum = 0
            for num, freq in top_x_items:
                top_x_sum += num*freq
            result.append(top_x_sum)

        return result