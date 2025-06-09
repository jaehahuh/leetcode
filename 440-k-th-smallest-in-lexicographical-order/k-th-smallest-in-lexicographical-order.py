class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # Prefix tree
        def get_count(prefix, n):
            curr = prefix
            next = prefix + 1
            count = 0
            while curr <= n:
                count += min(n+1, next) - curr
                curr *= 10
                next *= 10
            return count

        curr_num = 1
        k -= 1 # The first number is 1, so take one out in advance

        while k > 0:
            count = get_count(curr_num, n)
            if count <= k:
                curr_num += 1 # Pass this subtree and move to the side
                k -= count # Skipped one subtree
            else:
                curr_num *= 10 # Move to child in the subtree
                k -= 1 # count 
        return curr_num