class FolderNode:
    def __init__(self, name: str):
        self.name = name
        self.children = {} # 자식 폴더들: {이름: 노드 객체}
        self.is_deleted = False # 삭제 대상으로 마킹되었는지 여부

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # 1. 트리 구조 설계 및 구성
        root = FolderNode("")

        # 각 경로를 트리에 삽입
        for path_list in paths:
            current_node = root  # 각 path_list를 처리하기 전에 항상 root에서 시작
            for folder_name in path_list:
                if folder_name not in current_node.children:
                    # 새로운 폴더 노드 생성하여 자식으로 추가
                    current_node.children[folder_name] = FolderNode(folder_name)
                # 현재 노드를 방금 처리한 자식 노드로 이동
                current_node = current_node.children[folder_name]

        # 2. 중복 폴더 탐색 (Post-order Traversal 및 해싱)
        # 이 해시맵을 사용하여 중복되는 서브트리 구조를 가진 노드들을 탐색
        subtree_hashes = collections.defaultdict(list)

        # 재귀적으로 서브트리 해시를 계산하고 중복을 기록하는 DFS 함수
        def get_subtree_hash(node: FolderNode) -> str:
            # 자식 노드가 없는 경우 (리프 노드 또는 빈 폴더)
            if not node.children:
                return "" 

            # 자식 노드들을 이름 기준으로 정렬하여 일관된 해시를 생성
            child_hashes = []
            for child_name in sorted(node.children.keys()):
                child_node = node.children[child_name]
                # 자식 노드의 서브트리 해시를 재귀적으로 계산
                child_subtree_hash = get_subtree_hash(child_node)
                # (자식 이름 + 자식 서브트리 해시) 형태로 조합
                child_hashes.append(f"({child_name}{child_subtree_hash})")

            # 현재 노드의 서브트리 구조를 나타내는 해시 문자열을 생성
            current_subtree_hash_str = "".join(child_hashes)
            
            if current_subtree_hash_str:
                subtree_hashes[current_subtree_hash_str].append(node)
            
            return current_subtree_hash_str

        # 루트에서부터 DFS를 시작하여 모든 서브트리 해시를 계산
        get_subtree_hash(root)

        # 3. 중복 폴더 마킹
        # 이제 subtree_hashes 딕셔너리를 이용하여 실제 삭제할 폴더들을 마킹
        for hash_val, nodes_list in subtree_hashes.items():
            # 중복된 구조를 가진 폴더가 2개 이상인 경우 (즉, 동일한 해시를 가진 노드가 여러 개)
            if len(nodes_list) >= 2:
                # 이 구조를 가진 모든 최상위 폴더들을 삭제 대상으로 마킹
                for node_to_mark in nodes_list:
                    # 해당 노드 및 그 모든 하위 노드를 is_deleted = True로 설정
                    def mark_all_descendants_as_deleted(current_delete_node: FolderNode):
                        current_delete_node.is_deleted = True
                        for child_node_name in current_delete_node.children:
                            mark_all_descendants_as_deleted(current_delete_node.children[child_node_name])
                    
                    mark_all_descendants_as_deleted(node_to_mark)
        
        # 4. 남아 있는 폴더 경로 수집
        result = []

        def collect_remaining_paths(node: FolderNode, current_path_segments: List[str]):
            if node.is_deleted:
                return

            # 루트 노드가 아니라면 (이름이 ""가 아니라면), 현재 경로를 결과에 추가
            if node.name:
                result.append(current_path_segments + [node.name])

            # 자식 노드들을 순회하여 재귀적으로 경로를 수집
            for child_name in node.children:
                child_node = node.children[child_name]
                # 자식에게 전달될 새로운 경로 세그먼트를 생성
                # (루트 노드가 아니라면) 현재 노드 이름을 경로에 추가
                next_path_segments = current_path_segments + [node.name] if node.name else current_path_segments
                collect_remaining_paths(child_node, next_path_segments)

        collect_remaining_paths(root, [])

        return result