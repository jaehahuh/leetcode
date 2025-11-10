class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        stack = []

        for num in nums:
            # While the top of the stack is greater than the current number
            while stack and stack[-1] > num:
                stack.pop()
                operations += 1
            
            # If the stack is empty or the top is smaller than the current number
            if not stack or stack[-1] < num:
                # push the current number (ignore zeros and duplicate tops)
                if num > 0:
                    stack.append(num)

        # Each remaining value in the stack requires one operation to remove.
        operations += len(stack)  
        return operations