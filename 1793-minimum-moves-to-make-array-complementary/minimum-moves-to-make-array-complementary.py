class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)
    
        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]
            low = min(a, b) + 1
            high = max(a, b) + limit
            sum_ab = a + b
        
            # 초기 2번 변경 가정
            diff[2] += 2
            # 한 번 변경으로 가능한 구간 시작 -1
            diff[low] -= 1
            # 0번 변경 가능한 위치에 -1
            diff[sum_ab] -= 1
            # 0번 변경 가능 위치 바로 다음부터 +1
            diff[sum_ab + 1] += 1
            # 한 번 변경 가능 구간 종료 다음부터 +1
            diff[high + 1] += 1
        
        moves = float('inf')
        current = 0
        for x in range(2, 2 * limit + 1):
            current += diff[x]
            if current < moves:
                moves = current
        return moves