class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = Counter(nums)

        # Build events for inclusive integer intervals [L, R]
        events = []
        for a in nums:
            L = a - k
            R = a + k
            events.append((L, 1))
            events.append((R + 1, -1))  # use R+1 to make [L, R] inclusive

        events.sort()

        # Build segments where cover is constant: segments = [(start, end, cover), ...]
        segments = []
        cover = 0
        i = 0
        n_ev = len(events)
        # We'll track current coordinate; start new segment when cover changes
        while i < n_ev:
            x = events[i][0]
            # Between previous coordinate and x-1, cover was whatever it was before applying events at x.
            # But we need to know previous coordinate:
            if segments:
                prev_start, prev_end, prev_cov = segments[-1]
                # If the previous segment ended before x-1, it's already closed; otherwise we adjust end
                # (we will finalize previous end below when encountering next coordinate)
            # Apply all events at x
            delta = 0
            while i < n_ev and events[i][0] == x:
                delta += events[i][1]
                i += 1
            # After applying events at x, cover becomes:
            old_cover = cover
            cover += delta
            # We must create/extend segments representing integer coordinates where cover is constant.
            # There are two relevant integer ranges:
            # 1) If this is the first event, there might be no previous segment.
            # 2) After applying events at x, the cover value 'cover' applies starting at x (integer x).
            # We will set segment start = x and leave end to be determined when next event appears.
            # But we also need to ensure any gaps between events are captured: We'll manage segments as open-ended and finalize when next event seen.
            if not segments:
                # start new segment at x with cover value 'cover'
                segments.append([x, x, cover])
            else:
                # previous segment currently holds start..end; extend its end up to x-1 if needed.
                # Get last segment
                last = segments[-1]
                last_start, last_end, last_cov = last
                # If last_end < x-1, extend last_end to x-1 (cover in that range = last_cov)
                if last_end < x - 1:
                    last[1] = x - 1
                    # start a new segment at x with current cover
                    segments.append([x, x, cover])
                else:
                    # adjacent or overlapping: set last_end to x (so previous cover region includes x if last_cov == cover)
                    # But previous last_cov is the cover after previous events; cover now is updated.
                    # We should close previous segment at x-1 and start new at x with new cover.
                    last[1] = x - 1
                    segments.append([x, x, cover])

        # After processing all events, the last segment's end may be equal to its start; but cover beyond last event is stable as 'cover'.
        # We set last segment's end to a large value? Actually, beyond last event there is no element's interval covering further integers,
        # because events include all R+1 decrements. So cover after last event is correct only at that coordinate.
        # We leave segments as they are.

        # Normalize segments to tuples and remove any invalid ones where start > end
        segs = []
        for s in segments:
            start, end, cov = s
            if start <= end:
                segs.append((start, end, cov))
            else:
                # if start == end but we already adjusted, allow single-point if within integer
                # (if start == end, it's valid)
                if start == end:
                    segs.append((start, end, cov))

        if not segs:
            return 0

        # Build a list of segment starts for binary search
        starts = [s[0] for s in segs]

        res = 0

        # 1) For each unique nums value v, find the segment that contains v (if any) and calculate candidate using exact
        for v, exact in cnt.items():
            # find rightmost segment whose start <= v
            idx = bisect.bisect_right(starts, v) - 1
            if idx >= 0:
                st, ed, cov = segs[idx]
                if st <= v <= ed:
                    candidate = min(cov, exact + numOperations)
                    if candidate > res:
                        res = candidate
                else:
                    # v not inside any segment (should be rare). But then cover at v is 0 -> candidate = min(0, exact+numOperations) = 0
                    pass
            else:
                # no segment starts <= v -> cover 0
                pass

        # 2) For each segment, consider integers inside the segment that are NOT equal to any existing nums value.
        #    If there exists at least one integer in [start, end] that is not a key in cnt, we can pick it with exact=0:
        #    candidate = min(cov, numOperations)
        # To check quickly, we can count how many distinct nums fall into the segment using starts of unique sorted values.
        unique_vals = sorted(cnt.keys())
        # For each segment, find how many unique_vals are inside; if count < segment length+1 then there's at least one integer without exact.
        for st, ed, cov in segs:
            # number of integers in segment
            seg_len = ed - st + 1
            # count unique values inside segment via bisect on unique_vals
            lpos = bisect.bisect_left(unique_vals, st)
            rpos = bisect.bisect_right(unique_vals, ed)
            unique_inside = rpos - lpos
            if seg_len > unique_inside:
                # there exists an integer with exact = 0
                candidate = min(cov, numOperations)
                if candidate > res:
                    res = candidate

        return res