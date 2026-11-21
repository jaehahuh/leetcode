class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        tree = [[] for _ in range(n)]
        for node in range(1, n):
            tree[parent[node]].append(node)

        new_parent = parent[:]
        closest_ancestor = [-1] * 26

        def assign_new_parents(node: int) -> None:
            char_idx = ord(s[node]) - ord('a')
            prev_ancestor = closest_ancestor[char_idx]

            if node > 0 and prev_ancestor != -1:
                new_parent[node] = prev_ancestor

            closest_ancestor[char_idx] = node
            for child in tree[node]:
                assign_new_parents(child)
            closest_ancestor[char_idx] = prev_ancestor

        assign_new_parents(0)

        new_tree = [[] for _ in range(n)]
        for node in range(1, n):
            new_tree[new_parent[node]].append(node)

        sizes = [1] * n

        def calc_subtree_size(node: int) -> int:
            for child in new_tree[node]:
                sizes[node] += calc_subtree_size(child)
            return sizes[node]

        calc_subtree_size(0)
        return sizes