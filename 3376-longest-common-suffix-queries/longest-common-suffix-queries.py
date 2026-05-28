class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        global_best = 0
        min_len = len(wordsContainer[0])
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < min_len:
                min_len = len(wordsContainer[i])
                global_best = i
                
        # 트라이 노드 구조: [best_index, children_dict]
        root = [global_best, {}]
        
        # wordsContainer의 단어들을 뒤집어서 트라이에 삽입
        for i, word in enumerate(wordsContainer):
            curr = root
            w_len = len(word)
            
            for char in reversed(word):
                if char not in curr[1]:
                    # 처음 생성되는 노드라면 현재 단어의 인덱스로 초기화
                    curr[1][char] = [i, {}]
                curr = curr[1][char]
                
                # 이미 존재하는 노드라면, 현재 단어가 더 짧은지 비교하여 최적 인덱스 갱신
                # (길이가 같은 경우는 먼저 등장한 인덱스가 이미 저장되어 있으므로, 미만(<)일 때만 갱신)
                if w_len < len(wordsContainer[curr[0]]):
                    curr[0] = i
                    
        # wordsQuery의 단어들을 뒤집어서 트라이 탐색
        ans = []
        for query in wordsQuery:
            curr = root
            for char in reversed(query):
                if char in curr[1]:
                    curr = curr[1][char]
                else:
                    # 매칭되는 문자가 더 이상 없으면 탐색 중단
                    break
            # 현재 도달한 최적 노드의 인덱스를 결과에 추가
            ans.append(curr[0])
            
        return ans