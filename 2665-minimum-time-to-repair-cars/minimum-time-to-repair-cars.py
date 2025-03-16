class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def count_repaired(time):
            count = 0
            for rank in ranks:
                count += int(sqrt(time//rank)) # 각 정비사별 수리할 수 있는 자동차 수 계산
            return count

        left, right = 1, ranks[0] * (cars ** 2) 
        result = -1

        while left <= right:
            mid = (left + right) // 2
            repaired = count_repaired(mid)

            if repaired >= cars:
                result = mid   # 수리 가능하면 결과 업데이트
                right = mid - 1   # 더 작은 시간 탐색
            else:
                left = mid + 1 # 더 큰 시간 탐색
        
        return result