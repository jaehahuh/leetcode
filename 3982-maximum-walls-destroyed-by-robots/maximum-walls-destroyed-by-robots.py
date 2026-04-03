class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)

        # 왼쪽, 오른쪽 사거리 내 파괴 가능한 벽의 개수 배열 초기화
        left = [0] * n
        right = [0] * n

        # 인접한 두 로봇 간 중복 파괴 가능한 벽 개수 저장 (경계 조정을 위한 배열)
        overlapping = [0] * n
        
        # 로봇 위치 -> 사거리 매핑
        robot_distance_map = {robot_pos: dist for robot_pos, dist in zip(robots, distance)}

        robots.sort()
        walls.sort()

        for i in range(n):
            robot_pos = robots[i]
            dist = robot_distance_map[robot_pos]

            # 로봇 위치 기준 벽들의 인덱스
            right_bound_idx = bisect.bisect_right(walls, robot_pos)

            # 왼쪽 사거리 최대 범위
            if i > 0:
                left_limit = max(robot_pos - dist, robots[i - 1] + 1)
            else:
                left_limit = robot_pos - dist
            left_limit_idx = bisect.bisect_left(walls, left_limit)

             # 왼쪽 방향 사거리 내 파괴 가능한 벽 개수
            left[i] = right_bound_idx - left_limit_idx
            
            # 오른쪽 사거리 최대 범위
            if i < n - 1:
                right_limit = min(robot_pos + dist, robots[i + 1] - 1)
            else:
                right_limit = robot_pos + dist
            right_limit_idx = bisect.bisect_right(walls, right_limit)
            
            # 로봇 위치 기준 벽 인덱스
            left_bound_idx = bisect.bisect_left(walls, robot_pos)
            
            # 오른쪽 방향 사거리 내 파괴 가능한 벽 개수
            right[i] = right_limit_idx - left_bound_idx

            # 인접 로봇 간의 중복 파괴 벽 수 계산 
            if i > 0:
                prev_robot_pos = robots[i - 1]
                prev_robot_wall_idx = bisect.bisect_left(walls, prev_robot_pos)
                overlapping[i] = right_bound_idx - prev_robot_wall_idx
        
        # DP 변수 초기화
        max_left = left[0]
        max_right = right[0]
        
        # DP를 통한 로봇별 방향 선택 최적화
        for i in range(1, n):
            # 왼쪽 방향으로 쏘는 경우: 이전 로봇 왼쪽, 또는 이전 로봇 오른쪽에서 일부 조정
            current_left = max(
                max_left + left[i],
                max_right - right[i - 1] + min(left[i] + right[i - 1], overlapping[i])
            )
            # 오른쪽 방향으로 쏘는 경우: 이전까지 왼쪽이었거나 오른쪽이었을 때 최대값 계산
            current_right = max(max_left + right[i], max_right + right[i])
            
            max_left, max_right = current_left, current_right
        
        return max(max_left, max_right)