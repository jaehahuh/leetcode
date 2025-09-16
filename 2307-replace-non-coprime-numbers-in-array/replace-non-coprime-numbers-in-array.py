class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            curr = num
            while stack:
                gcd_num = gcd(stack[-1], curr)
                if gcd_num == 1:
                    break
                curr = (stack[-1]//gcd_num) * curr #lck
                stack.pop()
            stack.append(curr)
        
        return stack