class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []
        for i in range(len(words)):
            for char in words[i]:
                #If that one char is equal to x, put x in the list and break the loop.
                if char == x:
                    output.append(i)
                    break

        return output