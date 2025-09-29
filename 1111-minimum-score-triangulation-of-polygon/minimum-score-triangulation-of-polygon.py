class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        num_vertices = len(values) # 다각형의 꼭짓점 개수

        # dp[i][j]는 values[i]부터 values[j]까지의 부분 다각형 최소 삼각 분할 점수를 저장
        dp = [[0] * num_vertices for _ in range(num_vertices)]

        # span: 현재 부분 다각형의 길이 (꼭짓점 간의 거리), 2부터 시작 (최소 삼각형 구성)
        for span in range(2, num_vertices):
            # left_vertex_idx: 부분 다각형의 시작 꼭짓점 인덱스
            for left_vertex_idx in range(num_vertices - span):
                right_vertex_idx = left_vertex_idx + span # right_vertex_idx: 부분 다각형의 끝 꼭짓점 인덱스
                dp[left_vertex_idx][right_vertex_idx] = float('inf') # 최소 점수를 찾기 위해 무한대로 초기화

                # middle_vertex_idx: 부분 다각형을 분할하는 세 번째 꼭짓점 인덱스 (left_vertex_idx < middle_vertex_idx < right_vertex_idx)
                for middle_vertex_idx in range(left_vertex_idx + 1, right_vertex_idx):
                    # 현재 분할 방식의 총 점수 계산: 왼쪽 부분 + 오른쪽 부분 + 현재 형성되는 삼각형 점수
                    curr_tri_score = (
                        dp[left_vertex_idx][middle_vertex_idx] +
                        dp[middle_vertex_idx][right_vertex_idx] +
                        values[left_vertex_idx] * values[middle_vertex_idx] * values[right_vertex_idx])
                    
                    # 현재까지 찾은 최소 점수와 비교하여 갱신
                    dp[left_vertex_idx][right_vertex_idx] = min(
                        dp[left_vertex_idx][right_vertex_idx], curr_tri_score
                    )

        # dp[0][num_vertices - 1]에 전체 다각형의 최소 삼각 분할 점수가 저장됨
        return dp[0][num_vertices - 1]