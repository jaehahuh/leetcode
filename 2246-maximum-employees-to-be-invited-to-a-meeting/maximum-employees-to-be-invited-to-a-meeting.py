class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)

        # 1. Find longest cycle among employees
        longest_cycle = 0
        visited = [False] * n # Array to mark if an employee has been visited
        length_2_cycles = []  # List to store all 2-cycles (mutual favorite pairs)

        for i in range(n):
            if visited[i]:
                continue  # Skip if this employee has already been visited
            
            start_point = i  # Start point for the current cycle detection(it must be fixed)
            current = i   # Pointer to traverse the cycle
            current_set = set()

            # Traverse until we reach a visited node or detect a cycle
            while not visited[current]:
                visited[current] = True
                current_set.add(current)
                current = favorite[current]  # Move to the favorite employee

            # If the current node is part of the current traversal, we found a cycle
            if current in current_set:
                length = len(current_set) # Length of the entire traversal

                # Remove nodes outside the cycle
                while start_point != current: 
                    length -= 1
                    start_point = favorite[start_point]
                longest_cycle = max(longest_cycle, length)  # Update the longest cycle

                # If this is a 2-cycle, store it for later
                if length == 2:  
                    length_2_cycles.append([current, favorite[current]])
        
        # 2. Find sum of longest chains attached to 2-cycles (non-closed cycles)
        inverted = defaultdict(list) # To store the reversed graph
        for dst, src in enumerate(favorite):  # Build the inverted graph
            inverted[src].append(dst)
        
        def bfs(src, parent):
            """
            Perform a BFS from `src` while avoiding the `parent` node.
            Calculate the length of the longest chain starting from `src`.
            """

            q = deque([(src, 0)]) # node, length
            max_length = 0

            while q:
                node, length = q.popleft()
                if node == parent: # Skip the parent node to avoid revisiting
                    continue
                max_length = max(max_length, length) 
                for neighbor in inverted[node]: 
                    q.append((neighbor, length + 1))
            
            return max_length

        chain_sum = 0 # Sum of the longest chains attached to all 2-cycles

        # Add the lengths of chains starting from both nodes in the 2-cycle
        for node1, node2 in length_2_cycles: 
            chain_sum += bfs(node1, node2) + bfs(node2, node1) + 2 
            # +2 for the 2-cycle itself
        
        # Return the maximum of the longest cycle or the chain sum
        return max(chain_sum, longest_cycle)