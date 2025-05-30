class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dfs(node):
            distance = [-1] * len(edges)
            d = 0
            while node != -1 and distance[node] == -1:
                distance[node] = d
                d += 1
                node = edges[node]
            return distance
        
        dist1 = dfs(node1)
        dist2 = dfs(node2)

        min_max_dist = float('inf')
        result = -1

        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])

                if max_dist < min_max_dist:
                    min_max_dist = max_dist
                    result = i
                
                elif max_dist == min_max_dist and i < result:
                    result = i

        return result