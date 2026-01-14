import collections
from typing import List

class Node:
    __slots__ = ("range_left_idx", "range_right_idx", "coverage_count", "covered_length")

    def __init__(self):
        self.range_left_idx = self.range_right_idx = 0
        self.coverage_count = self.covered_length = 0


class SegmentTree:
    def __init__(self, sorted_coordinate_values):
        num_intervals = len(sorted_coordinate_values) - 1 
        self.coordinate_values = sorted_coordinate_values
        self.tree_nodes = [Node() for _ in range(num_intervals << 2)]
        self._build_tree(1, 0, num_intervals - 1)

    def _build_tree(self, node_idx, current_range_start_idx, current_range_end_idx):
        self.tree_nodes[node_idx].range_left_idx = current_range_start_idx
        self.tree_nodes[node_idx].range_right_idx = current_range_end_idx
        
        if current_range_start_idx != current_range_end_idx:
            mid_idx = (current_range_start_idx + current_range_end_idx) >> 1
            self._build_tree(node_idx << 1, current_range_start_idx, mid_idx)
            self._build_tree(node_idx << 1 | 1, mid_idx + 1, current_range_end_idx)

    def modify_coverage(self, node_idx, query_start_idx, query_end_idx, delta_coverage):
        if self.tree_nodes[node_idx].range_left_idx >= query_start_idx and self.tree_nodes[node_idx].range_right_idx <= query_end_idx:
            self.tree_nodes[node_idx].coverage_count += delta_coverage
        else:
            mid_idx = (self.tree_nodes[node_idx].range_left_idx + self.tree_nodes[node_idx].range_right_idx) >> 1
            if query_start_idx <= mid_idx:
                self.modify_coverage(node_idx << 1, query_start_idx, query_end_idx, delta_coverage)
            if query_end_idx > mid_idx:
                self.modify_coverage(node_idx << 1 | 1, query_start_idx, query_end_idx, delta_coverage)
        self._recalculate_covered_length(node_idx)

    def _recalculate_covered_length(self, node_idx):
        if self.tree_nodes[node_idx].coverage_count:
            self.tree_nodes[node_idx].covered_length = \
                self.coordinate_values[self.tree_nodes[node_idx].range_right_idx + 1] - \
                self.coordinate_values[self.tree_nodes[node_idx].range_left_idx]
        elif self.tree_nodes[node_idx].range_left_idx == self.tree_nodes[node_idx].range_right_idx:
            self.tree_nodes[node_idx].covered_length = 0
        else:
            self.tree_nodes[node_idx].covered_length = \
                self.tree_nodes[node_idx << 1].covered_length + \
                self.tree_nodes[node_idx << 1 | 1].covered_length

    @property
    def current_total_covered_length(self):
        return self.tree_nodes[1].covered_length


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        unique_x_coords = set()
        sweep_events = []
        for x_left, y_bottom, side_length in squares:
            x_right, y_top = x_left + side_length, y_bottom + side_length
            unique_x_coords.update([x_left, x_right])
            
            sweep_events.append((y_bottom, x_left, x_right, 1))
            sweep_events.append((y_top, x_left, x_right, -1))
        
        sweep_events.sort()
        
        sorted_x_values = sorted(list(unique_x_coords))
        
        x_coord_to_idx_map = {x_val: i for i, x_val in enumerate(sorted_x_values)}
        
        segment_tree = SegmentTree(sorted_x_values)
        
        total_unique_area = 0
        previous_y_pos = 0

        for current_y_pos, x_start_val, x_end_val, event_type in sweep_events:
            total_unique_area += (current_y_pos - previous_y_pos) * segment_tree.current_total_covered_length
            
            segment_tree.modify_coverage(1, x_coord_to_idx_map[x_start_val], x_coord_to_idx_map[x_end_val] - 1, event_type)
            
            previous_y_pos = current_y_pos
        
        target_half_area = total_unique_area / 2
        
        current_sum_of_area_below_line = 0
        previous_y_for_split_check = 0

        for current_y_pos, x_start_val, x_end_val, event_type in sweep_events:
            strip_area = (current_y_pos - previous_y_for_split_check) * segment_tree.current_total_covered_length
            
            if current_sum_of_area_below_line + strip_area >= target_half_area:
                remaining_area_to_reach_target = target_half_area - current_sum_of_area_below_line
                fractional_y_increase = remaining_area_to_reach_target / segment_tree.current_total_covered_length
                return previous_y_for_split_check + fractional_y_increase
            
            current_sum_of_area_below_line += strip_area
            segment_tree.modify_coverage(1, x_coord_to_idx_map[x_start_val], x_coord_to_idx_map[x_end_val] - 1, event_type)
            previous_y_for_split_check = current_y_pos
            
        return 0