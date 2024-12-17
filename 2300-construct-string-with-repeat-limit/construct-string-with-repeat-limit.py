import collections
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        result = []
        count_string = collections.Counter(s)

        # build a max heap with (-ASCII value, count) to prioritize larger characters
        max_heap = [(-ord(ch), count) for ch, count in count_string.items()]
        heapq.heapify(max_heap)

        while max_heap:
            #extract the largest character from the heap
            curr_char_val, curr_count = heapq.heappop(max_heap)
            curr_char = chr(-curr_char_val)
            
            # determine how many times to add the current character (up to repeatLimit)
            add_count = min(curr_count, repeatLimit)
            result.append(curr_char * add_count)
            
            # handle remaining characters and prevent consecutive repetitions
            if curr_count - add_count > 0 and max_heap:
                # extract the second largest character from the heap
                next_char_val, next_count = heapq.heappop(max_heap)
                next_char = chr(-next_char_val)
                result.append(next_char) 
                if next_count > 1:
                    heapq.heappush(max_heap, (next_char_val, next_count - 1))
                heapq.heappush(max_heap, (curr_char_val, curr_count - add_count))
        
        return ''.join(result)