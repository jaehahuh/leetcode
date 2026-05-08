class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        max_value = max(nums)

        # Helper function: generate a smallest prime factor of max value
        def build_spf(limit: int):
            spf = list(range(limit + 1))
            if limit >= 0:
                spf[0] = 0
            if limit >= 1:
                spf[0] = 1
            p = 2
            while p * p <= limit:
                if spf[p] == p:
                    for num in range(p*p, limit + 1, p):
                        if spf[num] == num:
                            spf[num] = p
                p += 1
            return spf
        
        # Helper function: extract different prime factor sets from spf
        def factorize_distinct(x: int, spf: List[int]):
            primes = set()
            while x > 1:
                primes.add(spf[x])
                x //= spf[x]
            return primes
        
        spf = build_spf(max_value)
        primes_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            if val <= 1:
                continue
            primes = factorize_distinct(val, spf)
            for p in primes:
                primes_to_indices[p].append(i)
        
        # BFS
        q = deque([0])
        visited = [False] * n
        visited[0] = True
        dist = [-1] * n
        dist[0] = 0

        while q:
            i = q.popleft()
            d = dist[i]
            if i == n - 1:
                return d

            # Adjacent step
            for neighbor in (i-1, i+1):
                if 0 <= neighbor < n and not visited[neighbor]:
                    visited[neighbor] = True
                    dist[neighbor] = d + 1
                    q.append(neighbor)
            
            # Prime teleportation
            val = nums[i]
            if val > 1 and spf[val] == val:
                p = val
                if p in primes_to_indices:
                    for j in primes_to_indices[p]:
                        if not visited[j]:
                            visited[j] = True
                            dist[j] = d + 1
                            q.append(j)
                
                    #Remove the prime p to avoid reprocessing
                    del primes_to_indices[p]

        return dist[n-1]