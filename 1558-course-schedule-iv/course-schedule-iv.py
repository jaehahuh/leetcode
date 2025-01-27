class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        # 인접 리스트로 그래프를 표현 (key: course, value: list of prerequisites)
        for prereq, course in prerequisites:
            adj[course].append(prereq)
    
        #DFS
        def dfs(current_course):
            if current_course not in prereq_map:
                prereq_map[current_course] = set() # 현재 과목의 모든 선행 조건을 저장
                # 현재 과목의 직접적인 선행 조건들에 대해 DFS 수행
                for prereq in adj[current_course]:
                    prereq_map[current_course] |= dfs(prereq) # 선행 조건을 합집합(union)으로 추가
                prereq_map[current_course].add(current_course)  # 자신도 자신의 선행 조건 집합에 추가
            return prereq_map[current_course]

        prereq_map = {}  # 각 과목마다 선행 조건을 저장할 맵 (key: course, value: set of prerequisites)
        for i in range(numCourses):
            dfs(i)

        result = []
        for u, v in queries:
            # u가 v의 선행 조건인지 확인
            result.append(u in prereq_map[v]) # v의 선행 조건 집합에 u가 포함되면 True

        return result 