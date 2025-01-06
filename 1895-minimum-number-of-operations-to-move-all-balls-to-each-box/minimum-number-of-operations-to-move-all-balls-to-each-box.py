class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0] * len(boxes)
    
        left_balls, left_moves = 0,0
        for i in range(len(boxes)):
            result[i] += left_moves
            if boxes[i] == '1':
                left_balls += 1
            left_moves += left_balls
       
        right_balls, right_moves = 0,0
        for i in range(len(boxes)-1, -1, -1):
            result[i] += right_moves
            if boxes[i] == '1':
                right_balls += 1
            right_moves += right_balls

        return result   