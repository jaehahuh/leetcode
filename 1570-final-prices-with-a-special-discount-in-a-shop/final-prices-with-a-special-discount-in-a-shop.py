class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices[:]
        stack = []
        for i in range(len(prices)-1, -1, -1):
            # remove elements from the stack that are greater than the current price
            while stack and stack[-1] > prices[i]:
                stack.pop()
            # apply the discount if the stack is not empty 
            if stack:
                result[i] -= stack[-1]
            # push the current price onto the stack for future comparisons
            stack.append(prices[i])
            
        return result