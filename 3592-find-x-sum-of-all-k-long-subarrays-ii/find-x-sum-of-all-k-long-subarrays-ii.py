class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        if x == k:
            # k == x 이면 각 윈도우 합을 바로 반환
            s = sum(nums[:k])
            res = [s]
            for i in range(k, n):
                s += nums[i] - nums[i-k]
                res.append(s)
            return res

        cnt = defaultdict(int)   # value -> count
        in_top = set()           # 현재 top에 포함된 값들
        sum_top = 0              # top에 속한 값들의 value * count 합

        top_heap = []   # min-heap of (count, value) for top group
        rest_heap = []  # max-heap via (-count, -value, value) for rest group

        def clean_top():
            while top_heap:
                c, v = top_heap[0]
                if v not in in_top or cnt[v] != c:
                    heapq.heappop(top_heap)
                else:
                    break

        def clean_rest():
            while rest_heap:
                nc, nv, v = rest_heap[0]
                if cnt[v] != -nc or v in in_top:
                    heapq.heappop(rest_heap)
                else:
                    break

        def get_top_worst():
            clean_top()
            return top_heap[0] if top_heap else None  # (count, value)

        def get_rest_best():
            clean_rest()
            if not rest_heap: return None
            nc, nv, v = rest_heap[0]
            return (-nc, v)

        def promote_from_rest():
            nonlocal sum_top
            rb = get_rest_best()
            if not rb: return False
            c, v = rb
            heapq.heappop(rest_heap)
            in_top.add(v)
            sum_top += cnt[v] * v
            heapq.heappush(top_heap, (cnt[v], v))
            return True

        def demote_from_top():
            nonlocal sum_top
            tw = get_top_worst()
            if not tw: return False
            c, v = tw
            heapq.heappop(top_heap)
            in_top.discard(v)
            sum_top -= cnt[v] * v
            heapq.heappush(rest_heap, (-cnt[v], -v, v))
            return True

        # 초기 윈도우 구성
        for i in range(k):
            v = nums[i]
            cnt[v] += 1
        # 초기 rest에 모두 넣기
        for v, c in cnt.items():
            heapq.heappush(rest_heap, (-c, -v, v))
        # top을 x개 채우기
        while len(in_top) < x and promote_from_rest():
            pass
        # 교환 가능한 경우 교체 반복
        while True:
            tw = get_top_worst()
            rb = get_rest_best()
            if not tw or not rb: break
            c_t, v_t = tw
            c_r, v_r = rb
            if (c_r > c_t) or (c_r == c_t and v_r > v_t):
                demote_from_top()
                promote_from_rest()
            else:
                break

        res = [sum_top]

        # 슬라이드
        for i in range(k, n):
            add = nums[i]
            rem = nums[i-k]

            # 제거 처리
            cnt[rem] -= 1
            if rem in in_top:
                # top에 있던 원소는 sum_top에서 값만큼 빼줌
                sum_top -= rem
                if cnt[rem] == 0:
                    in_top.discard(rem)
                else:
                    heapq.heappush(top_heap, (cnt[rem], rem))
            else:
                if cnt[rem] > 0:
                    heapq.heappush(rest_heap, (-cnt[rem], -rem, rem))

            # 추가 처리
            cnt[add] += 1
            if add in in_top:
                sum_top += add
                heapq.heappush(top_heap, (cnt[add], add))
            else:
                heapq.heappush(rest_heap, (-cnt[add], -add, add))

            # top 크기 맞추기
            while len(in_top) < x and promote_from_rest():
                pass
            # 더 우수한 rest가 있으면 교체
            while True:
                tw = get_top_worst()
                rb = get_rest_best()
                if not tw or not rb: break
                c_t, v_t = tw
                c_r, v_r = rb
                if (c_r > c_t) or (c_r == c_t and v_r > v_t):
                    demote_from_top()
                    promote_from_rest()
                else:
                    break

            res.append(sum_top)

        return res