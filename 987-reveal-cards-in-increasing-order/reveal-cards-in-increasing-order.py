import collections

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        #initialize result
        result = [None] * len(deck) 
        deck.sort()
        #this queue helps in managing the position of cards in the final result
        queue = collections.deque(range(len(deck)))

        #revealing the Cards:
        for num in deck:
            i = queue.popleft()
            result[i] = num
            # if there are still indices left in the queue
            if queue:
                #pop the next index and append it to the end of the queue
                skip = queue.popleft()
                queue.append(skip)

        return result