class RMQ:
    def __init__(self, data, func):
        self.func = func
        self.st = [data]
        n = len(data)
        j = 1
        while (1 << j) <= n:
            prev = self.st[-1]
            curr = [func(prev[i], prev[i + (1 << (j - 1))]) for i in range(len(prev) - (1 << (j - 1)))]
            self.st.append(curr)
            j += 1

    def query(self, l, r):
        if l > r: 
            return None
        j = (r - l + 1).bit_length() - 1
        return self.func(self.st[j][l], self.st[j][r - (1 << j) + 1])

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')
        
        blocks = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            blocks.append({'type': int(s[i]), 'start': i, 'end': j - 1, 'length': j - i})
            i = j
            
        block_idx = [0] * n
        for idx, b in enumerate(blocks):
            for k in range(b['start'], b['end'] + 1):
                block_idx[k] = idx
                
        M = len(blocks)
        
        Z_len = [b['length'] if b['type'] == 0 else 0 for b in blocks]
        O_len = [b['length'] if b['type'] == 1 else float('inf') for b in blocks]
        
        S_len = [0] * M
        for idx in range(1, M - 1):
            if blocks[idx]['type'] == 1:
                S_len[idx] = blocks[idx-1]['length'] + blocks[idx+1]['length']
                
        rmq_Z = RMQ(Z_len, max)
        rmq_O = RMQ(O_len, min)
        rmq_S = RMQ(S_len, max)

        ans = []
        
        for l, r in queries:
            idx_l = block_idx[l]
            idx_r = block_idx[r]
            
            if idx_l == idx_r:
                ans.append(total_ones)
                continue
                
            len_L = blocks[idx_l]['end'] - l + 1
            len_R = r - blocks[idx_r]['start'] + 1
            
            z_max = 0
            if blocks[idx_l]['type'] == 0: z_max = max(z_max, len_L)
            if blocks[idx_r]['type'] == 0: z_max = max(z_max, len_R)
            
            res_Z = rmq_Z.query(idx_l + 1, idx_r - 1)
            if res_Z is not None: z_max = max(z_max, res_Z)
                
            o_min = rmq_O.query(idx_l + 1, idx_r - 1)
            
            if o_min is None or o_min == float('inf'):
                ans.append(total_ones)
                continue
                
            max_s = 0
            
            first_O = idx_l + 1 if blocks[idx_l + 1]['type'] == 1 else idx_l + 2
            last_O = idx_r - 1 if blocks[idx_r - 1]['type'] == 1 else idx_r - 2
            
            def get_z_len(i):
                if i == idx_l: return len_L
                if i == idx_r: return len_R
                return blocks[i]['length'] if blocks[i]['type'] == 0 else 0
                
            if first_O <= last_O:
                max_s = max(max_s, get_z_len(first_O - 1) + get_z_len(first_O + 1))
                
                if first_O != last_O:
                    max_s = max(max_s, get_z_len(last_O - 1) + get_z_len(last_O + 1))
                    
                if first_O + 2 <= last_O - 2:
                    res_S = rmq_S.query(first_O + 2, last_O - 2)
                    if res_S is not None: 
                        max_s = max(max_s, res_S)
                        
            gain = max(max_s, z_max - o_min)
            ans.append(total_ones + gain)
            
        return ans