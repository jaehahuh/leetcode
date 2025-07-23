class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        max_points = 0

        def remove_substring(curr_s, first_char, second_char, point):
            nonlocal max_points
            stack = []

            for ch in curr_s:
                if stack and ch == second_char and stack[-1] == first_char:
                    stack.pop()
                    max_points += point
                else:
                    stack.append(ch)
            
            return ''.join(stack)

        if x >= y:
            remain_s = remove_substring(s, 'a', 'b', x)
            remove_substring(remain_s, 'b', 'a', y)

        else:
            remain_s = remove_substring(s, 'b', 'a', y)
            remove_substring(remain_s, 'a', 'b', x)
    
        return max_points