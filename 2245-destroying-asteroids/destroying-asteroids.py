class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort(reverse = True)
        total = mass + sum(asteroids)
        for m in asteroids:
            total -= m
            if total < m:
                return False
        return True