class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #split s by space
        word_list = s.split(" ")
        #if last index of list is word, return length of word 
        if word_list[-1].isalpha():
            return len(word_list[-1])

        # if last index of list is not word (empty string), 
        # then move the index from the back of the list to the front until the word comes out.
        else:
            for i in range(len(word_list)-1,-1,-1):
                if word_list[i].isalpha():
                    return len(word_list[i])
            
            #if s is has no words or if it's a word made up of space, then return 0
            return 0
