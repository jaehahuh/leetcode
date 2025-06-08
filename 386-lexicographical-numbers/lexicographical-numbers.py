class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        num = 1
        for _ in range(1, n+1):
            result.append(num)
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        
        return result