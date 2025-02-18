class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        
        for i in range(len(pattern)+1):
            stack.append(i + 1)
            # stack is not empty and either index at the end of the pattern or the current pattern character is 'I'
            while stack and  (i == len(pattern) or pattern[i] == 'I'):
                result.append(str(stack.pop()))

        return ''.join(result)