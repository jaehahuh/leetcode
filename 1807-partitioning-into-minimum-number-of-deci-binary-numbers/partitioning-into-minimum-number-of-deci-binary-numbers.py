class Solution:
    def minPartitions(self, n: str) -> int:
        #consider the largest number(maximum digits) in n.
        return int(max(n))