class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        list1 = [(r,c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        list2 = [(r,c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        if not list1 or not list2:
            return 0
        
        counts = Counter((r2 - r1, c2 - c1) for r1, c1 in list1 for r2, c2 in list2)
        return max(counts.values()) if counts else 0