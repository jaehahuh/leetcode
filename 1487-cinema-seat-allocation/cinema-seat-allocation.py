class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(int)
        for row, seat in reservedSeats:
            reserved[row] |= (1 << seat)
        
        possible_groups = (n-len(reserved)) * 2 #예약이 없는 row

        # 2,3,4,5번 좌석 비트마스크: (1<<2) | (1<<3) | (1<<4) | (1<<5) = 60
        left_mask = 60
        # 6,7,8,9번 좌석 비트마스크: (1<<6) | (1<<7) | (1<<8) | (1<<9) = 960
        right_mask = 960
        # 4,5,6,7번 좌석 비트마스크: (1<<4) | (1<<5) | (1<<6) | (1<<7) = 240
        middle_mask = 240

        for mask in reserved.values():
            left_empty = (mask & left_mask) == 0
            right_empty = (mask & right_mask) == 0
            
            if left_empty and right_empty:
                possible_groups += 2
            elif left_empty or right_empty or ((mask & middle_mask) == 0):
                possible_groups += 1
                
        return  possible_groups