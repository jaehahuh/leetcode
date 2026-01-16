class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7

        all_h_fences = sorted(list(set(hFences) | {1, m}))
        possible_heights = set()
        for i in range(len(all_h_fences)):
            for j in range(i + 1, len(all_h_fences)):
                possible_heights.add(all_h_fences[j] - all_h_fences[i])
        
        all_v_fences = sorted(list(set(vFences) | {1, n}))
        possible_widths = set()
        for i in range(len(all_v_fences)):
            for j in range(i + 1, len(all_v_fences)):
                possible_widths.add(all_v_fences[j] - all_v_fences[i])

        max_side_length = 0
        for length in possible_heights:
            if length in possible_widths:
                max_side_length = max(max_side_length, length)
        
        if max_side_length == 0:
            return -1
        
        return (max_side_length * max_side_length) % MOD