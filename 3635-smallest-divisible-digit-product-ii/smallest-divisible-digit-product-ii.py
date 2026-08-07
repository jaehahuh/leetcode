class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        def get_factors(n):
            cnt = {2: 0, 3: 0, 5: 0, 7: 0}
            for p in cnt:
                while n % p == 0:
                    cnt[p] += 1
                    n //= p
            return cnt, n
        
        req, rem = get_factors(t)
        if rem > 1: return "-1" 
        
        df = {d: get_factors(d)[0] for d in range(1, 10)}
        
        @cache
        def get_23(c2, c3):
            if c2 <= 0 and c3 <= 0: return []
            best = None
            for d, cost2, cost3 in [(9,0,2), (8,3,0), (6,1,1), (4,2,0), (3,0,1), (2,1,0)]:
                if (cost2 and c2 > 0) or (cost3 and c3 > 0):
                    res = sorted(get_23(max(0, c2 - cost2), max(0, c3 - cost3)) + [d])
                    if not best or len(res) < len(best) or (len(res) == len(best) and res < best):
                        best = res
            return best

        def make_suffix(r2, r3, r5, r7, max_l):
            s = [5] * r5 + [7] * r7
            if len(s) > max_l: return None
            s += get_23(r2, r3)
            if len(s) > max_l: return None
            return "".join(map(str, sorted(s + [1] * (max_l - len(s)))))

        n_len = len(num)
        pref = [{2: 0, 3: 0, 5: 0, 7: 0}]
        for x in num:
            if x == '0': break
            pref.append({p: pref[-1][p] + df[int(x)][p] for p in req})

        for i in range(len(pref) - 1, -1, -1):
            if i == n_len: 
                if all(pref[i][p] >= req[p] for p in req): return num
                continue
                
            curr = int(num[i])
            for d in range(curr + 1, 10):
                rem_f = {p: max(0, req[p] - pref[i][p] - df[d][p]) for p in req}
                suffix = make_suffix(rem_f[2], rem_f[3], rem_f[5], rem_f[7], n_len - 1 - i)
                # 수정된 부분: 빈 문자열("")도 통과하도록 is not None으로 체크
                if suffix is not None:
                    return num[:i] + str(d) + suffix

        L = n_len + 1
        while True:
            suffix = make_suffix(req[2], req[3], req[5], req[7], L)
            if suffix is not None: return suffix
            L += 1