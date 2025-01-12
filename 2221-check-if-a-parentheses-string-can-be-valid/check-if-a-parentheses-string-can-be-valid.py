class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        stack_1 = []  #cannot change - index of '(' 
        stack_0 = []  #can change

        for i in range(len(s)):
            if locked[i] == '0':
                stack_0.append(i)
            elif s[i] == "(":
                stack_1.append(i)
            else:
                if stack_1:
                    stack_1.pop()
                elif stack_0:
                    stack_0.pop()
                else:
                    return False
            
        while stack_1 and stack_0 and stack_1[-1] < stack_0[-1]:
            stack_1.pop()
            stack_0.pop()
        if stack_1:
            return False
            
        return True