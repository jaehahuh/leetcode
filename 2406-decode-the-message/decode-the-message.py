class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_dic = {}
        n = ord('a')
        #build substitution table
        for ch in key:
            if ch != ' ' and ch not in key_dic:
                key_dic[ch] = chr(n)
                n += 1
        
        decode = ''
        #decode the message
        for ch in message:
            if ch == ' ':
                decode += ' '
            else:
                decode += key_dic[ch]
        
        return decode