class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apple = sum(apple)
        total_boxes = 0
        capacity.sort(reverse=True)
        n = len(capacity)
        for i in range(n):
            total_boxes += capacity[i]
            if total_boxes >= total_apple:
                return i + 1
        
        return n