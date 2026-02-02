class MinValueContainer:
    def __init__(self, size: int):
        self.size = size                   # 유지할 최소 원소 개수
        self.lower = SortedList()          # 가장 작은 size개의 원소를 담음
        self.upper = SortedList()          # 그 외 나머지 원소들
        self.current_sum = 0               # lower에 담긴 원소들의 합

    def balance(self):
        # lower의 크기가 size보다 작으면 upper에서 가장 작은 원소를 lower로 이동
        while len(self.lower) < self.size and len(self.upper) > 0:
            val = self.upper[0]
            self.upper.remove(val)
            self.lower.add(val)
            self.current_sum += val

        # lower의 크기가 size보다 크면 lower에서 가장 큰 원소를 upper로 이동
        while len(self.lower) > self.size:
            val = self.lower[-1]
            self.lower.remove(val)
            self.upper.add(val)
            self.current_sum -= val

    def add(self, val: int):
        # val을 lower 또는 upper에 해당 조건에 맞게 추가
        if len(self.upper) > 0 and val >= self.upper[0]:
            self.upper.add(val)
        else:
            self.lower.add(val)
            self.current_sum += val
        self.balance()

    def remove(self, val: int):
        # val을 제거하며 current_sum도 갱신
        if val in self.lower:
            self.lower.remove(val)
            self.current_sum -= val
        elif val in self.upper:
            self.upper.remove(val)
        self.balance()

    def get_sum(self) -> int:
        # 현재 lower에 담겨있는 size개의 원소 합 반환
        return self.current_sum


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        container = MinValueContainer(k - 2)

        # 초기화: 두 번째 부분배열 시작부터 (k-1 번째 시작 전까지) 원소들 추가
        for idx in range(1, k - 1):
            container.add(nums[idx])

        # 초기 답안 구성: container가 가진 합 + k번째 부분배열 시작 원소 비용
        answer = container.get_sum() + nums[k - 1]

        # k번째 부분배열부터 배열 끝까지 반복하며 최소 비용 갱신
        for i in range(k, n):
            j = i - dist - 1  # dist 초과 인덱스는 제거 대상
            if j > 0:
                container.remove(nums[j])
            container.add(nums[i - 1])
            answer = min(answer, container.get_sum() + nums[i])

        # 첫 번째 부분배열 시작 원소 비용 더해 최종 결과 반환
        return answer + nums[0]