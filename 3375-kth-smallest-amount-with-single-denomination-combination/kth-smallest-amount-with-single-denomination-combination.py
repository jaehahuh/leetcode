class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        # 모든 동전 조합의 (최소공배수, 부호) 정보를 미리 계산
        # 부호는 홀수 개 선택 시 +1, 짝수 개 선택 시 -1
        subsets = []
        for i in range(1, 1 << n):
            lcm_val = 1
            count = 0
            for j in range(n):
                if (i >> j) & 1:
                    lcm_val = math.lcm(lcm_val, coins[j])
                    count += 1
            sign = 1 if count % 2 == 1 else -1
            subsets.append((lcm_val, sign))

        # x 이하의 금액 중 만들 수 있는 금액의 총 개수를 구하는 함수
        def count_amounts(x: int) -> int:
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (x // lcm_val)
            return total

        # 이진 탐색으로 k번째 금액(최소 x)을 찾음
        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_amounts(mid) >= k:
                ans = mid
                high = mid - 1  # 더 작은 x가 존재하는지 탐색
            else:
                low = mid + 1

        return ans