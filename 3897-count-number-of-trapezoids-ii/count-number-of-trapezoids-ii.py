from fractions import Fraction
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        s_i = defaultdict(list)
        m_s = defaultdict(list)

        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1

                if dx != 0:
                    s = dy/dx
                    b = (y1 * dx - x1 * dy)/ dx

                else:
                    s = inf
                    b = x1

                s_i[s].append(b)
                mid = (x1 + x2, y1 + y2)
                m_s[mid].append(s)
        
        result = 0
        for intercepts_in_same_slope in s_i.values():
            if len(intercepts_in_same_slope) == 1: continue
            c = Counter(intercepts_in_same_slope)

            acc = 0
            for count in c.values():
                result += acc * count
                acc += count
        
        for slope_in_same_mid in m_s.values():
            if len(slope_in_same_mid) == 1: continue
            c = Counter(slope_in_same_mid)

            acc = 0
            for count in c.values():
                result -= acc * count
                acc += count
        
        return result