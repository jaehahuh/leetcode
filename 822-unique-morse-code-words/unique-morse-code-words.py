class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
                    ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--",
                    "-..-","-.--","--.."]
        
        alpha_list = []
        for i in range(26):
            alpha_list.append(chr(ord('a')+i))
        
        code_dict = dict(zip(alpha_list, morse_code))
        transformation_list = []

        for i in range(len(words)):
            transformation = ''
            for j in range(len(words[i])):
                transformation += code_dict[words[i][j]]
            transformation_list.append(transformation)
        
        unique_list = set(transformation_list)
        return len(unique_list)