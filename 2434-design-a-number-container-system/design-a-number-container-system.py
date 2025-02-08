from collections import deque 
class NumberContainers:

    def __init__(self):
        self.number_to_index = {}
        self.index_to_number = {} 

    def change(self, index: int, number: int) -> None:
        # Check if the index was previously assigned to a different number
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number in self.number_to_index:
                heapq.heappush(self.number_to_index[old_number], float('inf')) 

        # Update the new number for the index
        self.index_to_number[index] = number
        if number not in self.number_to_index:
            self.number_to_index[number] = []
        heapq.heappush(self.number_to_index[number], index)
  
    def find(self, number: int) -> int:
        if number not in self.number_to_index or not self.number_to_index[number]:
            return -1
        # Remove invalid indices and return the smallest valid index
        while self.number_to_index[number] and self.index_to_number.get(self.number_to_index[number][0]) != number:
            heapq.heappop(self.number_to_index[number])
            
        return self.number_to_index[number][0] if self.number_to_index[number] else -1
        

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)