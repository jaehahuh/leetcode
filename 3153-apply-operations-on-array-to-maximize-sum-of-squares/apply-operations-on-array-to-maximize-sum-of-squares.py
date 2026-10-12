class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
    
        # 각 비트(0 ~ 30)별로 1의 개수를 저장
        bit_counts = [0] * 31
        for x in nums:
            for i in range(31):
                if (x >> i) & 1:
                    bit_counts[i] += 1
                    
        # k개의 숫자를 만듦 (초기값은 모두 0)
        max_nums = [0] * k
        for i in range(31):
            count = bit_counts[i]
            # 비트 i의 1 개수만큼, 앞에서부터 차례대로 숫자에 비트를 켬
            for j in range(count):
                if j < k:
                    max_nums[j] |= (1 << i)
                    
        # 최종 k개 원소의 제곱의 합 계산
        ans = 0
        for x in max_nums:
            ans = (ans + x * x) % MOD
            
        return ans