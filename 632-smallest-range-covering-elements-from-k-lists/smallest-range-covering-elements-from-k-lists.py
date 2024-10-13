import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 우선순위 큐 초기화: (값, 리스트 인덱스, 원소 인덱스)
        heap = []
        max_val = float('-inf')

        # 각 리스트의 첫 번째 원소를 힙에 넣는다
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])

        # 결과 범위 초기화 (시작, 끝)
        result_range = [-float('inf'), float('inf')]

        while heap:
            min_val, list_idx, elem_idx = heapq.heappop(heap)

            # 현재 범위 갱신
            if max_val - min_val < result_range[1] - result_range[0]:
                result_range = [min_val, max_val]

            # 해당 리스트의 다음 원소가 있는지 확인
            if elem_idx + 1 == len(nums[list_idx]):
                break

            # 다음 원소를 힙에 추가
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            max_val = max(max_val, next_val)

        return result_range
