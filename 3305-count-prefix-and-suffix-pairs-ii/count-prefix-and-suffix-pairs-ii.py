# TrieNode는 children nodes를 저장할 딕셔너리와 현재 노드의 문자열 개수를 저장
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0 

class Trie:
    # root node를 초기화
    def __init__(self):
        self.root = TrieNode()
    
    # Trie에 문자열을 삽입
    def add(self, word):
        curr = self.root

        #for start_char, end_char in zip(word, reversed(word)):
        for i in range(len(word)):
            start_char = word[i]  # 문자열의 i번째 문자
            end_char = word[len(word)-i-1]  # 문자열의 끝에서 i번째 문자
            # (start_char, end_char) 쌍이 현재 노드의 자식에 없으면 새로 추가
            if (start_char, end_char) not in curr.children:
                curr.children[(start_char, end_char)] = TrieNode()
            curr = curr.children[(start_char, end_char)] # 다음 노드로 이동
            curr.count += 1 # 현재 노드를 경유하는 문자열 개수를 증가
    
    # Trie에서 주어진 문자열이 prefix이자 suffix인 문자열의 개수를 반환
    def count(self, word):
        curr = self.root
        #for start_char, end_char in zip(word, reversed(word)):
        for i in range(len(word)):
            start_char = word[i]
            end_char = word[len(word)-i-1]
            if (start_char, end_char) not in curr.children:
                return 0
            curr = curr.children[(start_char, end_char)]
        # 현재 노드의 count 값을 반환 (매칭된 문자열의 개수)
        return curr.count
     
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        root = Trie() # Trie 구조 생성
        for word in reversed(words):
            # 현재 단어로 prefix와 suffix를 만족하는 문자열 개수 추가
            result += root.count(word)
            # 현재 단어를 Trie에 삽입
            root.add(word)

        return result