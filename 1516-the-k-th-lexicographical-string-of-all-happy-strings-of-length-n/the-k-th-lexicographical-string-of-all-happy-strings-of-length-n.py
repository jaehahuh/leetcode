class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = ['a', 'b', 'c']
        total = 3 * (2 ** (n - 1))
        if k > total:
            return ""

        result = []
        def dfs(pos, prev_char, k):
            if pos == n:
                return True, k  # 완성

            for c in chars:
                if c == prev_char:
                    continue
                # 뒤에 올 수 있는 문자열 수
                count = 2 ** (n - pos - 1)
                if k > count:
                    k -= count
                else:
                    result.append(c)
                    return dfs(pos + 1, c, k)
            return False, k

        # 첫 문자 처리
        for c in chars:
            count = 2 ** (n - 1)
            if k > count:
                k -= count
            else:
                result.append(c)
                dfs(1, c, k)
                break

        return "".join(result)