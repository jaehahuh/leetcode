class DSU:
    def __init__(self, parent):
        self.parent = parent
    
    def find(self, x):
        # 경로 압축 적용하며 루트 노드 찾기
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def join(self, x, y):
        # 두 노드가 속한 집합 합치기
        px = self.find(x)
        py = self.find(y)
        self.parent[px] = py

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        ans = -1

        # 간선이 최소 n-1개는 있어야 연결 가능
        if len(edges) < n - 1:
            return - 1
        
        # 반드시 포함해야 하는 간선과 선택 가능한 간선 분리
        mustEdges = [e for e in edges if e[3] == 1]
        optionalEdges = [e for e in edges if e[3] == 0]

        # must 간선 수가 너무 많으면 사이클 가능성으로 불가능
        if len(mustEdges) > n - 1:
            return -1
        
         # 선택 가능한 간선은 강도 내림차순 정렬 (강한 간선부터 선택)
        optionalEdges.sort(key=lambda x: x[2], reverse=True)

         # must 간선을 우선 연결
        dsuInit = DSU(list(range(n)))
        selectedInit = 0
        mustMinStability = 200000  # 크게 잡은 최대 안정성 초기값

        for u, v, s, must in mustEdges:
            # 사이클 발생 시 불가능
            if dsuInit.find(u) == dsuInit.find(v) or selectedInit == n - 1:
                return -1
            dsuInit.join(u, v)
            selectedInit += 1
            mustMinStability = min(mustMinStability, s)  # must 간선 중 최소 강도 저장

        # 이분 탐색: 최소 간선 강도가 최소 mustMinStability 이하일 때 탐색
        l = 0
        r = mustMinStability

        while l < r:
            mid = l + ((r - l + 1) >> 1)
            dsu = DSU(dsuInit.parent[:])  # must 간선 연결 정보 복사
            selected = selectedInit
            doubledCount = 0  # 업그레이드 사용 횟수

            for u, v, s, must in optionalEdges:
                if dsu.find(u) == dsu.find(v):
                    continue
                
                # 강도가 mid 이상이면 그냥 연결
                if s >= mid:
                    dsu.join(u, v)
                    selected += 1
                
                # 아니면 업그레이드 여유 있을 때 2배해서 연결 가능 여부 판단
                elif doubledCount < k and s * 2 >= mid:
                    doubledCount += 1
                    dsu.join(u, v)
                    selected += 1
                else:
                    continue  # 연결 불가, 다음 간선 검사
                
                if selected == n - 1:
                    break
            
            # 스패닝 트리 완성 여부에 따른 이분 탐색 범위 조절
            if selected == n - 1:
                ans = mid
                l = mid
            else:
                r = mid - 1

        return ans
