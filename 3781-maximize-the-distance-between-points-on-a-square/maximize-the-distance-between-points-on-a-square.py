class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        linear_points = []
        for x, y in points:
            if y == 0: dist = x
            elif x == side: dist = side + y
            elif y == side: dist = 2 * side + (side - x)
            else: dist = 3 * side + (side - y)
            linear_points.append(dist)
        
        linear_points.sort()
        n = len(linear_points)
        total_perimeter = 4 * side

        def can_place(min_dist):
            limit_val = linear_points[0] + (total_perimeter // k)
            
            for i in range(n):
                if linear_points[i] > limit_val:
                    break

                count = 1
                last_pos = linear_points[i]
                first_pos = linear_points[i]
                
                curr_idx = i + 1
                for _ in range(k - 1):
                    target = last_pos + min_dist
                    next_idx = bisect.bisect_left(linear_points, target, lo=curr_idx)
                    
                    if next_idx < n:
                        count += 1
                        last_pos = linear_points[next_idx]
                        curr_idx = next_idx + 1
                    else:
                        break
                if count == k:
                    if (total_perimeter - (last_pos - first_pos)) >= min_dist:
                        return True
            return False

        low = 1
        high = total_perimeter // k
        ans = 1
        
        while low <= high:
            mid = (low + high) // 2
            if mid == 0:
                low = 1
                continue
            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans