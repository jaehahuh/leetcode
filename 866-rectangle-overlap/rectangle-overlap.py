class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (
            rec1[2] <= rec2[0] or  # 왼쪽
            rec1[0] >= rec2[2] or  # 오른쪽
            rec1[3] <= rec2[1] or  # 아래
            rec1[1] >= rec2[3]     # 위
        )