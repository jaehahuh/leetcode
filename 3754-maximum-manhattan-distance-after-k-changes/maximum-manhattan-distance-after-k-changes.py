class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        directions = [('N', 'E'), ('N', 'W'), ('S', 'E'), ('S', 'W')]
        max_dist = 0

        for dir1, dir2 in directions:
            current_distance = 0  # 현재까지 누적 거리
            changes_left = k      # 남은 방향 변경 횟수
            for ch in s:
                if ch == dir1 or ch == dir2:
                    current_distance += 1  # 원래 방향이니까 그대로 진행
                elif changes_left > 0:
                    # 선호 방향으로 바꿔서 거리 증가
                    changes_left -= 1
                    current_distance += 1
                else:
                    current_distance -= 1   # 방향도 다르고 변경 기회도 없으면 거리 감소

                max_dist = max(max_dist, current_distance)

        return max_dist