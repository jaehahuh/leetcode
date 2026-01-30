class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)

        # 모든 원본, 목표 문자열 + source, target 포함하여 고유 부분문자열 ID 매핑
        subToId = {}
        def getId(s):
            if s not in subToId:
                subToId[s] = len(subToId)
            return subToId[s]
        
        getId(source)
        getId(target)
        for s in original:
            getId(s)
        for s in changed:
            getId(s)
        
        subCount = len(subToId)

        # 비용 인접 행렬 초기화
        dist = [[math.inf] * subCount for _ in range(subCount)]
        for i in range(subCount):
            dist[i][i] = 0

        # 변환 규칙 적용
        for o, c, w in zip(original, changed, cost):
            u = subToId[o]
            v = subToId[c]
            dist[u][v] = min(dist[u][v], w)

        # Floyd-Warshall 알고리즘으로 모든 변환 간 최소 비용 계산
        for k in range(subCount):
            for i in range(subCount):
                if dist[i][k] == math.inf:
                    continue
                for j in range(subCount):
                    if dist[k][j] == math.inf:
                        continue
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        dp = [math.inf] * (n + 1)
        dp[0] = 0   # 처음에서 아무 변환도 하지 않은 상태

        # 길이별 가능한 부분 문자열 길이를 미리 구함
        subLengths = sorted(set(len(s) for s in original))

        for i in range(n):
            if dp[i] == math.inf:
                continue
            # 원래 문자와 목표 문자가 같으면 비용 없이 넘어갈 수 있음
            if source[i] == target[i]:
                if dp[i + 1] > dp[i]:
                    dp[i + 1] = dp[i]

            # 가능한 부분 문자열 길이마다 검사
            for length in subLengths:
                if i + length > n:
                    continue
                s_sub = source[i:i+length]
                t_sub = target[i:i+length]
                if s_sub in subToId and t_sub in subToId:
                    u = subToId[s_sub]
                    v = subToId[t_sub]
                    cost_uv = dist[u][v]
                    if cost_uv == math.inf:
                        continue
                    if dp[i + length] > dp[i] + cost_uv:
                        dp[i + length] = dp[i] + cost_uv

        return dp[n] if dp[n] != math.inf else -1