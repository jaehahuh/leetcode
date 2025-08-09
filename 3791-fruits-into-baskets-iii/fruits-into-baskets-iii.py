class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)

        # 세그먼트 트리 리프 기준 인덱스(2의 거듭제곱 크기로 올림)
        leaf_base = 1
        while leaf_base < n:
            leaf_base <<= 1

        # 구간 최대를 저장하는 세그먼트 트리 배열
        tree_max = [0] * (2 * leaf_base)

        # 리프에 바구니 용량 배치
        for idx, capacity in enumerate(baskets):
            tree_max[leaf_base + idx] = capacity

        # 내부 노드(구간 최대) 빌드
        for node in range(leaf_base - 1, 0, -1):
            left_val = tree_max[2 * node]
            right_val = tree_max[2 * node + 1]
            tree_max[node] = left_val if left_val >= right_val else right_val

        def find_leftmost(required):
            # 루트가 required보다 작으면, 전체에 조건을 만족하는 바구니가 없음
            if tree_max[1] < required:
                return -1

            node = 1
            # 리프까지 내려가며 왼쪽 자식부터 검사
            while node < leaf_base:
                left_child = 2 * node
                if tree_max[left_child] >= required:
                    node = left_child
                else:
                    node = left_child + 1
            return node - leaf_base  # 리프 위치 → 원래 인덱스

        def update_to_zero(index: int) -> None:
            node = index + leaf_base
            tree_max[node] = 0
            node //= 2
            while node:
                left_val = tree_max[2 * node]
                right_val = tree_max[2 * node + 1]
                tree_max[node] = left_val if left_val >= right_val else right_val
                node //= 2

        # 과일을 왼쪽 → 오른쪽 순으로 배치 시도
        unplaced_count = 0
        for quantity in fruits:
            basket_idx = find_leftmost(quantity)
            if basket_idx == -1:
                unplaced_count += 1
            else:
                update_to_zero(basket_idx)

        return unplaced_count