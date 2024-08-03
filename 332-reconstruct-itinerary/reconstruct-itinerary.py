class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(deque)

        #sort the tickets to maintain lexical order
        for dep,arr in sorted(tickets):
            graph[dep].append(arr)
        
        route = []
        def dfs(dep):
            #check all destinations from depature
            while graph[dep]:
                 # get the next destination with the smallest lexical order
                dfs(graph[dep].popleft())

            # add next destination with the smallest lexical order
            route.append(dep)
            
        dfs('JFK')

        #route is in reverse order, so reverse it to get the right order
        return route[::-1]