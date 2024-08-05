class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        #Set to track nodes that have already been fully processed
        visited = set()
        
        #Set to track nodes currently in the DFS path
        path =  set()

        def dfs(course):
            # Return False if the current node is already in the path as it has a cycle
            if course in path:
                return False

            # Return True if the current node has already been processed
            if course in visited:
                return True

            # Add the current node to the path
            path.add(course)

            #DFS for adjacent Nodes on the current node
            for pre in graph[course]:
                if not dfs(pre):
                    return False

            # Remove the current node from the path and mark it as processed
            path.remove(course)
            visited.add(course)
            return True

        #DFS with all subjects as starting points to see if there is a cycle
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True