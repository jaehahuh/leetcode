class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        
        converted_table = list(zip(original, changed,cost))
        for x, y, z in converted_table:
            dist[ord(x) - ord('a')][ord(y) - ord('a')] = min(dist[ord(x) - ord('a')][ord(y) - ord('a')], z)

        # Floyd-Warshall algorithm
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
         
        result = 0
        n = len(source)
        for s_char, t_char in zip(source, target):
            s_index = ord(s_char) - ord('a')
            t_index = ord(t_char) - ord('a')

            if s_index == t_index:
                continue
            if dist[s_index][t_index] == INF:
                return -1
            
            result += dist[s_index][t_index]
        
        return result