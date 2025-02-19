class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        comb_count = 3 * (2**(n-1))

        result = []
        choices = 'abc'
        left, right = 1, comb_count

        for i in range(n):
            curr = left
            partition_size = (right - left + 1) // len(choices)

            for letter in choices:
                if k in range(curr, curr + partition_size):
                    result.append(letter)
                    left = curr
                    right = curr + partition_size - 1
                    choices = 'abc'.replace(letter, '')
                    break
                curr += partition_size

        return ''.join(result)