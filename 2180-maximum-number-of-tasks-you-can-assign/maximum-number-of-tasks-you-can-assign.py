class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)

        # 2) k개의 작업을 수행할 수 있는지 검사
        def can_assign(k: int) -> bool:
            i = 0
            available = deque()
            pills_left = pills

            # 가장 강한 k명의 worker 순회
            for w in workers[m - k : m]:
                # 이 worker가 (알약 사용 포함) 처리 가능한 모든 작업을 큐에 추가
                while i < k and tasks[i] <= w + strength:
                    available.append(tasks[i])
                    i += 1

                # 처리할 작업이 없다면 실패
                if not available:
                    return False

                # 알약 없이 처리 가능한 가장 작은 작업이면 할당
                if available[0] <= w:
                    available.popleft()
                # 아니면, 알약을 써서 처리할 수 있는 가장 큰 작업에 알약 사용
                elif pills_left > 0:
                    pills_left -= 1
                    available.pop()
                else:
                    return False

            return True

        # 3) 이진 탐색으로 최대 수행 가능한 작업 수 찾기
        low, high = 0, min(n, m)
        while low < high:
            mid = (low + high + 1) // 2
            if can_assign(mid):
                low = mid
            else:
                high = mid - 1

        return low