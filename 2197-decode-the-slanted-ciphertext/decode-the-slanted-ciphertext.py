class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        
        originalText = []
        cols = len(encodedText)//rows
        
        for i in range(cols):
            curr_row, curr_col = 0, i
            while curr_row < rows and curr_col < cols:
                index = curr_row * cols + curr_col
                originalText.append(encodedText[index])

                curr_row += 1
                curr_col += 1
        
        return ''.join(originalText).rstrip()