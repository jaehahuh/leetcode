class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Build tree 
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Bob simulation - DFS
        bob_times = {} # node -> time visited
        def dfs(src, prev, time):
            # If Bob reaches the root 
            if src == 0:
                bob_times[src] = time
                return True
            
            for neighbor in graph[src]:
                if neighbor == prev:
                    continue # Skip the previous node
                
                # Recursively explore the next node
                if dfs(neighbor, src, time + 1):
                    bob_times[src] = time # Record the visit time for the current node
                    return True
            return False
        dfs(bob, -1, 0)

        #Alice simulation - BFS
        q = deque([(0, 0, -1, amount[0])])  #(node, time, parent, total profit)
        max_income = float('-inf')

        while q:
            node, time, parent, profit = q.popleft()
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue # Skip the parent node
                neighbor_profit = amount[neighbor] # Profit from the neighbor node
                neighbor_time = time + 1  # Visit time for the neighbor node

                # Compare with Bob's visit time
                if neighbor in bob_times:
                    if neighbor_time > bob_times[neighbor]:
                        neighbor_profit = 0  # If Bob arrives first, profit is 0
                    if neighbor_time == bob_times[neighbor]:
                        neighbor_profit //= 2 # If arriving simultaneously, halve the profit
                
                # Add the next node to the queue
                q.append((neighbor, neighbor_time, node, profit + neighbor_profit))

                # Update maximum income if it's a leaf node (no children)
                if len(graph[neighbor]) == 1:
                    max_income = max(max_income, profit + neighbor_profit)

        return max_income