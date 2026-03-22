class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4): # Check all possible rotations(0, 90, 180, 270 degrees)
            if mat == target:
                return True
 
            mat = [list(row[::-1]) for row in zip(*mat)] # Rotate the matrix 90 degrees clockwise
        
        return False