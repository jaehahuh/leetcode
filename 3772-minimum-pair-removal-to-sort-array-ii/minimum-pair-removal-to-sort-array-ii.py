class LinkedListNode:
    def __init__(self, value: int, original_index: int):
        self.value = value
        self.original_index = original_index
        self.previous_node = None
        self.next_node = None

class MergeCandidate:
    def __init__(self, left_node: LinkedListNode, right_node: LinkedListNode, potential_merged_value: int):
        self.left_node = left_node
        self.right_node = right_node
        self.potential_merged_value = potential_merged_value

    def __lt__(self, other: 'MergeCandidate') -> bool:
        if self.potential_merged_value == other.potential_merged_value:
            return self.left_node.original_index < other.left_node.original_index
        return self.potential_merged_value < other.potential_merged_value


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return 0

        priority_queue = []
        is_original_index_merged = [False] * n
        num_non_decreasing_violations = 0
        operations_count = 0

        head_node = LinkedListNode(nums[0], 0)
        current_node = head_node

        for i in range(1, n):
            new_node = LinkedListNode(nums[i], i)
            current_node.next_node = new_node
            new_node.previous_node = current_node

            heapq.heappush(
                priority_queue,
                MergeCandidate(current_node, new_node, current_node.value + new_node.value)
            )

            if current_node.value > new_node.value:
                num_non_decreasing_violations += 1

            current_node = new_node

        while num_non_decreasing_violations > 0:
            candidate = heapq.heappop(priority_queue)
            
            left_node_to_merge = candidate.left_node
            right_node_to_merge = candidate.right_node
            current_merged_value = candidate.potential_merged_value

            if (is_original_index_merged[left_node_to_merge.original_index] or
                is_original_index_merged[right_node_to_merge.original_index] or
                left_node_to_merge.value + right_node_to_merge.value != current_merged_value):
                continue

            operations_count += 1

            if left_node_to_merge.value > right_node_to_merge.value:
                num_non_decreasing_violations -= 1

            previous_node_of_left = left_node_to_merge.previous_node
            if previous_node_of_left:
                was_violation_before = previous_node_of_left.value > left_node_to_merge.value
                is_violation_after = previous_node_of_left.value > current_merged_value

                if was_violation_before and not is_violation_after:
                    num_non_decreasing_violations -= 1
                elif not was_violation_before and is_violation_after:
                    num_non_decreasing_violations += 1

            next_node_of_right = right_node_to_merge.next_node
            if next_node_of_right:
                was_violation_before = right_node_to_merge.value > next_node_of_right.value
                is_violation_after = current_merged_value > next_node_of_right.value

                if was_violation_before and not is_violation_after:
                    num_non_decreasing_violations -= 1
                elif not was_violation_before and is_violation_after:
                    num_non_decreasing_violations += 1

            left_node_to_merge.value = current_merged_value
            is_original_index_merged[right_node_to_merge.original_index] = True

            left_node_to_merge.next_node = next_node_of_right
            if next_node_of_right:
                next_node_of_right.previous_node = left_node_to_merge

            if previous_node_of_left:
                heapq.heappush(
                    priority_queue,
                    MergeCandidate(previous_node_of_left, left_node_to_merge,
                                   previous_node_of_left.value + left_node_to_merge.value)
                )
            if next_node_of_right:
                heapq.heappush(
                    priority_queue,
                    MergeCandidate(left_node_to_merge, next_node_of_right,
                                   left_node_to_merge.value + next_node_of_right.value)
                )

        return operations_count