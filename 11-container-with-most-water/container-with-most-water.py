class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        areas = []
   
        while left <= right:            
            area = min(height[left],height[right]) * (right - left)
            areas.append(area) 
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max(areas)
   