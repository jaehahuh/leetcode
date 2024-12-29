class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7  # Return results modulo 10^9 + 7 to prevent overflow

        # Dictionary to store the frequency of each character at each column
        # Key: (index, char), Value: frequency of char at index across all words
        count = defaultdict(int)
        for word in words:
            for index, char in enumerate(word):
                count[(index, char)] += 1  # Increment frequency for the given character and index

        dp = {}  # Memoization dictionary to store the results of (i, k)
        # i: current index of the target, k: current index of words (column-wise traversal)

        # DFS function for recursion
        def dfs(i, k):
            # Base Case 1: All characters in the target are processed
            if i == len(target):
                return 1  # Successfully formed the target string
            # Base Case 2: All columns of the words are exhausted
            if k == len(words[0]):
                return 0  # No way to form the target

            # If the state (i, k) is already computed, return the cached result
            if (i, k) in dp:
                return dp[(i, k)]

            # Current character in the target string
            t = target[i]

            # Case 1: Skip the current column
            dp[(i, k)] = dfs(i, k + 1)

            # Case 2: Use the current column if it contains the target character
            if (k, t) in count:  # Check if the character exists in the current column
                dp[(i, k)] += count[(k, t)] * dfs(i + 1, k + 1)

            # Return the result modulo mod to prevent overflow
            return dp[(i, k)] % mod

        # Start the DFS traversal from the first character of target and first column of words
        return dfs(0, 0)