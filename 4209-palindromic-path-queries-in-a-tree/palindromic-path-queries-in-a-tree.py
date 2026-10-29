
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        s = list(s)
        parent = [0] * n
        depth = [0] * n
        tin, tout, order = [0] * n, [0] * n, []

        # 반복문 DFS: Euler Tour
        stack = [(0, 0, False)]
        while stack:
            u, p, exiting = stack.pop()

            if exiting:
                tout[u] = len(order)
                continue

            parent[u] = p
            tin[u] = len(order)
            order.append(u)

            stack.append((u, p, True))
            for v in reversed(graph[u]):
                if v != p:
                    depth[v] = depth[u] + 1
                    stack.append((v, u, False))

        # 이진 리프팅용 조상 테이블
        LOG = n.bit_length()
        up = [parent[:]]
        for k in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[u]] for u in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = up[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u, v = up[k][u], up[k][v]

            return parent[u]

        # 루트부터 각 노드까지의 문자 XOR
        path = [0] * n
        for u in order:
            bit = 1 << (ord(s[u]) - ord('a'))
            path[u] = bit ^ (path[parent[u]] if u else 0)

        # XOR 펜윅 트리: 구간 갱신 + 점 조회
        fenwick = [0] * (n + 1)

        def add(i, value):
            i += 1
            while i <= n:
                fenwick[i] ^= value
                i += i & -i

        def get(i):
            result = 0
            i += 1
            while i:
                result ^= fenwick[i]
                i -= i & -i
            return result

        def update_subtree(u, value):
            add(tin[u], value)
            if tout[u] < n:
                add(tout[u], value)

        answer = []

        for q in queries:
            parts = q.split()
            u = int(parts[1])

            if parts[0] == "update":
                c = parts[2]
                old = 1 << (ord(s[u]) - ord('a'))
                new = 1 << (ord(c) - ord('a'))

                update_subtree(u, old ^ new)
                s[u] = c

            else:
                v = int(parts[2])
                w = lca(u, v)

                mask = (path[u] ^ get(tin[u]))
                mask ^= path[v] ^ get(tin[v])
                mask ^= 1 << (ord(s[w]) - ord('a'))

                answer.append(mask.bit_count() <= 1)

        return answer
