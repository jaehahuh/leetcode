class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # exact counts
        count_dict = Counter(nums)

        # build events for inclusive intervals [a-k, a+k]
        events = defaultdict(int)
        for a in nums:
            L = a - k
            R = a + k
            events[L] += 1
            events[R + 1] -= 1  # R inclusive -> decrement at R+1

        # merge and sort keys (events + nums) to examine all relevant coordinates
        all_keys = sorted(set(events.keys()) | set(count_dict.keys()))

        result = 0
        cover = 0
        keys = all_keys
        m = len(keys)

        for idx, x in enumerate(keys):
            # apply all events at x first so cover reflects intervals that include x
            if x in events:
                cover += events[x]

            # candidate at x (if some nums equal x)
            exact = count_dict.get(x, 0)
            if cover > 0:
                # number of convertible non-exact elements covering x = cover - exact (>=0)
                convertible = max(0, cover - exact)
                candidate = exact + min(numOperations, convertible)
            else:
                candidate = exact 
            if candidate > result:
                result = candidate

            # consider integers strictly between x and next_x-1 (if any)
            if idx + 1 < m:
                next_x = keys[idx + 1]
                if next_x - x >= 2:
                    # there exists at least one integer in (x, next_x-1)
                    # for such integers exact = 0, so candidate = min(cover, numOperations)
                    gap_candidate = min(cover, numOperations)
                    if gap_candidate > result:
                        result = gap_candidate

        return result