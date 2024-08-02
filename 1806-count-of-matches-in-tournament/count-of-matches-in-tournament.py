class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = n//2
        total_matches = matches
        while matches != 0:
            n = (n//2) + (n%2)
            matches = n//2
            total_matches += matches
        
        return total_matches