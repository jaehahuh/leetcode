class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {ch:i for i, ch in enumerate(s)} # Store the last index of each character
        partition = []
        size = 0  # Current partition size
        current_end = 0 # End index of the current partition

        for i, ch in enumerate(s):
            size += 1
            # Update the end index for the current character
            current_end = max(current_end, last_index[ch])

            if i == current_end:
                partition.append(size)  # Add the current partition size to the list
                size = 0 # Reset size

        return partition  