class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        #reverse each row
        for i in range(len(image)):
            image[i] = list(reversed(image[i]))

        #invert the image
        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                    print(image)
                else:
                    image[i][j] = 0
        return image