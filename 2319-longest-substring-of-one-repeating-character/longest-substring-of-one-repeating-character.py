class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        # tree[i] = [max_len, prefix_char, prefix_len, suffix_char, suffix_len]
        tree = [None] * (4 * n)

        def merge(L, R, len_L, len_R):
            mx = max(L[0], R[0])
            p_char, p_len = L[1], L[2]
            s_char, s_len = R[3], R[4]
            
            if L[3] == R[1]: # 왼쪽 경계 끝과 오른쪽 경계 시작이 같을 때
                mid_len = L[4] + R[2]
                mx = max(mx, mid_len)
                if L[2] == len_L: p_len = len_L + R[2]
                if R[4] == len_R: s_len = len_R + L[4]
                
            return [mx, p_char, p_len, s_char, s_len]

        def build(node, l, r):
            if l == r:
                c = s[l]
                tree[node] = [1, c, 1, c, 1]
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1], mid - l + 1, r - mid)

        def update(node, l, r, idx, char):
            if l == r:
                tree[node] = [1, char, 1, char, 1]
                return
            mid = (l + r) // 2
            if idx <= mid: update(2 * node, l, mid, idx, char)
            else: update(2 * node + 1, mid + 1, r, idx, char)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1], mid - l + 1, r - mid)

        build(1, 0, n - 1)
        
        ans = []
        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(tree[1][0]) 
            
        return ans