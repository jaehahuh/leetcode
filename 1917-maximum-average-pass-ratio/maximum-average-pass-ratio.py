
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # calculates percentage increaces in a class
        def calculate_increase(pass_count, total_count):
            return (pass_count + 1)/(total_count + 1) - pass_count/total_count
        
        # Build max-heap based on increase in pass ratio
        heap = []
        for pass_count, total_count in classes:
            increase = calculate_increase(pass_count, total_count)
            #Since the heapq module provides a mini-heap structure, 
            #change it to get the maximum heap by adding minus sign in front of it.
            #(ratio increase, number of pass students, total number of students)
            heapq.heappush(heap, (-increase, pass_count, total_count))
        
        # Distribute extra students
        for _ in range(extraStudents):
            increase, pass_count, total_count = heapq.heappop(heap)

            pass_count += 1
            total_count += 1

            new_increase = calculate_increase(pass_count,total_count)
            heapq.heappush(heap, (-new_increase, pass_count, total_count))
        
        # Calculate the final average pass ratio
        total_ratio = 0
        for increase, pass_count, total_count in heap:
            total_ratio += (pass_count / total_count)
        
        return total_ratio/len(classes)
            