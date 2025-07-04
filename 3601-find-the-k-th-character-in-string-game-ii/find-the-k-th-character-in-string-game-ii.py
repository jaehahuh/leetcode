class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1
        lengths = [1]  # Initial length of word = "a"
        for op in operations:
            if lengths[-1] > k + 1:
                lengths.append(lengths[-1] * 2)
            else:
                lengths.append(min(lengths[-1] * 2, k + 2))
        
        shift_count = 0

        for i in range(len(operations) - 1, -1, -1):
            current_op = operations[i]
            prev_len = lengths[i]

            if k >= prev_len:
                k -= prev_len
                if current_op == 1:
                    shift_count += 1

            if k == 0 and prev_len == 1:
                break

        final_char_code = (shift_count) % 26
        return chr(ord('a') + final_char_code)