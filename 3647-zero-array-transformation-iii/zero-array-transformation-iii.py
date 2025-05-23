class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        start_to_ends = defaultdict(list)
        
        # 각 쿼리의 시작 위치별로 끝 위치들을 모아둠
        for start, end in queries:
            start_to_ends[start].append(end)
        
        # 현재 커버 상태를 추적하는 배열 (line sweep용)
        coverage_diff = [0] * (n + 1)
        max_heap = []
        current_coverage = 0
        
        for i, needed in enumerate(nums):
            # i 위치에서 시작하는 쿼리들을 heap에 추가 (끝 위치 기준 max heap)
            if i in start_to_ends:
                for end in start_to_ends[i]:
                    heappush(max_heap, -end)  # max heap 구현 위해 음수로 저장
            
            # line sweep 누적합 업데이트 (여기선 coverage_diff[i] 누적)
            current_coverage += coverage_diff[i]
            
            # i 위치를 만족시키기 위해 필요한 커버 수만큼 heap에서 쿼리 사용
            while current_coverage < needed:
                # 사용할 쿼리가 없거나 현재 위치를 커버하지 못하면 불가능
                if not max_heap or -max_heap[0] < i:
                    return -1
                farthest_end = -heappop(max_heap)
                current_coverage += 1
                # 쿼리의 커버 범위가 끝난 위치 이후부터 커버 감소 표시
                coverage_diff[farthest_end + 1] -= 1
        
        # heap에 남아있는 쿼리 개수가 제거 가능한 최대 개수
        return len(max_heap)