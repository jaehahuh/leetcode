class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            s = str(i)
            # 유효하지 않은 숫자가 포함되면 탈락
            if '3' in s or '4' in s or '7' in s:
                continue
            # 변하는 숫자가 하나라도 있으면 Good Integer
            if '2' in s or '5' in s or '6' in s or '9' in s:
                count += 1
        return count