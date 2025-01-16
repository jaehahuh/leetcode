class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        indices_stable = []
        for i in range(1, len(height)):
            if height[i-1] > threshold:
                indices_stable.append(i)
        return indices_stable