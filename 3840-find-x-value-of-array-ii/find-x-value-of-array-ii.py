class Node:
    def __init__(self, k):
        self.k = k
        self.prod = 1
        self.remain = [0] * k

class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree = [Node(k) for _ in range(4 * self.n)]
        self._build(nums, 0, 0, self.n - 1)

    def _merge(self, left_node, right_node):
        res = Node(self.k)
        res.prod = (left_node.prod * right_node.prod) % self.k
        
        # 왼쪽 노드의 나머지 빈도 그대로 복사
        for i in range(self.k):
            res.remain[i] = left_node.remain[i]
            
        # 오른쪽 노드의 나머지들에 왼쪽 전체 곱을 곱한 결과 반영
        for i in range(self.k):
            new_rem = (i * left_node.prod) % self.k
            res.remain[new_rem] += right_node.remain[i]
            
        return res

    def _build(self, nums, node, lo, hi):
        if lo == hi:
            self.tree[node].prod = nums[lo] % self.k
            self.tree[node].remain = [0] * self.k
            self.tree[node].remain[nums[lo] % self.k] = 1
            return
        
        mid = (lo + hi) // 2
        self._build(nums, 2 * node + 1, lo, mid)
        self._build(nums, 2 * node + 2, mid + 1, hi)
        self.tree[node] = self._merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def update(self, i, val):
        self._update(0, 0, self.n - 1, i, val)

    def _update(self, node, lo, hi, i, val):
        if lo == hi:
            self.tree[node].prod = val % self.k
            self.tree[node].remain = [0] * self.k
            self.tree[node].remain[val % self.k] = 1
            return
        
        mid = (lo + hi) // 2
        if i <= mid:
            self._update(2 * node + 1, lo, mid, i, val)
        else:
            self._update(2 * node + 2, mid + 1, hi, i, val)
        self.tree[node] = self._merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, i, j):
        return self._query(0, 0, self.n - 1, i, j)

    def _query(self, node, lo, hi, i, j):
        if i <= lo and hi <= j:
            return self.tree[node]
        if j < lo or hi < i:
            # 범위 밖인 경우 항등원 반환 (곱셈의 항등원은 1)
            dummy = Node(self.k)
            dummy.prod = 1
            dummy.remain = [0] * self.k
            return dummy
        
        mid = (lo + hi) // 2
        left_res = self._query(2 * node + 1, lo, mid, i, j)
        right_res = self._query(2 * node + 2, mid + 1, hi, i, j)
        return self._merge(left_res, right_res)

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        tree = SegmentTree(nums, k)
        n = len(nums)
        ans = []
        
        for index, value, start, x in queries:
            tree.update(index, value)
            
            res_node = tree.query(start, n - 1)
            ans.append(res_node.remain[x])
            
        return ans