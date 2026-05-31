from sortedcontainers import SortedList
from typing import List

class SegmentTree:
    def __init__(self, tree_size: int):
        self.tree_size = tree_size
        self.max_gaps = [0] * (2 * tree_size)
        
    def update_gap(self, position: int, new_gap_size: int):
        position += self.tree_size
        self.max_gaps[position] = new_gap_size
        position //= 2
        
        while position > 0:
            self.max_gaps[position] = max(self.max_gaps[2 * position], self.max_gaps[2 * position + 1])
            position //= 2
            
    def get_max_gap(self, start: int, end: int) -> int:
        start += self.tree_size
        end += self.tree_size
        largest_gap = 0
        
        while start < end:
            if start % 2 == 1:
                largest_gap = max(largest_gap, self.max_gaps[start])
                start += 1
            if end % 2 == 1:
                end -= 1
                largest_gap = max(largest_gap, self.max_gaps[end])
            start //= 2
            end //= 2
            
        return largest_gap


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        max_coordinate = max([query[1] for query in queries]) + 1
        
        gap_segment_tree = SegmentTree(max_coordinate)
        sorted_obstacles = SortedList([0])
        results = []
        
        for query in queries:
            if query[0] == 1:
                obstacle_pos = query[1]
                insert_index = sorted_obstacles.bisect_right(obstacle_pos)
                left_obstacle = sorted_obstacles[insert_index - 1]
                
                gap_segment_tree.update_gap(obstacle_pos, obstacle_pos - left_obstacle)
                
                if insert_index < len(sorted_obstacles):
                    right_obstacle = sorted_obstacles[insert_index]
                    gap_segment_tree.update_gap(right_obstacle, right_obstacle - obstacle_pos)
                    
                sorted_obstacles.add(obstacle_pos)
                
            else:
                target_position = query[1]
                required_block_size = query[2]
                
                insert_index = sorted_obstacles.bisect_right(target_position)
                left_obstacle = sorted_obstacles[insert_index - 1]
                
                max_gap_in_range = gap_segment_tree.get_max_gap(0, left_obstacle + 1)
                gap_to_target = target_position - left_obstacle
                
                max_available_space = max(max_gap_in_range, gap_to_target)
                results.append(max_available_space >= required_block_size)
                
        return results