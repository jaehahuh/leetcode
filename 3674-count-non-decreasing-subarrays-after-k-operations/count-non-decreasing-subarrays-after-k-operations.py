class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        result = 0
        cost = 0

        dq = deque()

        right = n - 1
        # 오른쪽에서 왼쪽으로 순회
        for left in range(n - 1, -1, -1):

            # 새로운 왼쪽 원소보다 작은 그룹들을 합침
            while dq and nums[dq[-1]] < nums[left]:

                prev = dq.pop()

                # 제거한 그룹의 오른쪽 경계
                boundary = dq[-1] if dq else right + 1

                # 해당 그룹을 현재 값까지 증가시키는 비용
                cost += (boundary - prev) * (
                    nums[left] - nums[prev]
                )

            # 새로운 그룹 추가
            dq.append(left)

            # 연산 횟수가 k를 초과하면 오른쪽 축소
            while cost > k:

                # 오른쪽 끝 원소를 제거하면서 비용 감소
                cost -= nums[dq[0]] - nums[right]

                # 해당 그룹이 비었다면 덱에서 제거
                if dq[0] == right:
                    dq.popleft()

                right -= 1

            # 현재 left를 시작점으로 하는 유효한 부분 배열 개수
            result += right - left + 1

        return result