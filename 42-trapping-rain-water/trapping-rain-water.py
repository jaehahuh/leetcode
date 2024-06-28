class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] #store height index
        volume = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break

                width = i - stack[-1] - 1
                length = min(height[i], height[stack[-1]]) - height[top]

                volume += width * length
            stack.append(i)
        
        return volume