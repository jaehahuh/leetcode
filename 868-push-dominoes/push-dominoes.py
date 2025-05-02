class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        result = list(dominoes)

        boundaries = [-1] # Left virtual boundary 'L'
        for i, ch in enumerate(dominoes):
            if ch in ('L', 'R'):
                boundaries.append(i)
        boundaries.append(n)  # right virtual boundary 'R'

        # Process each segment between two boundary dominoes
        for k in range(len(boundaries) - 1):
            i, j = boundaries[k], boundaries[k + 1]

            # Get actual domino values (virtual boundaries default to 'L' or 'R')
            left = 'L' if i == -1 else result[i]
            right = 'R' if j == n else result[j]

            # Process the segment between i and j (exclusive)
            if left == 'R' and right == 'L':
                # Falling toward each other: fill from both ends
                l, r = i + 1, j - 1
                while l < r:
                    result[l] = 'R'
                    result[r] = 'L'
                    l += 1
                    r -= 1
            elif left == 'R' and right == 'R':
                # All dominoes fall to the right
                for idx in range(i + 1, j):
                    result[idx] = 'R'
            elif left == 'L' and right == 'L':
                # All dominoes fall to the left
                for idx in range(i + 1, j):
                    result[idx] = 'L'

        return ''.join(result)