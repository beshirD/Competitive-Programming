class Solution:
    def floodFill(self, image, sr, sc, newColor):
        neighbours = [[1,0],[-1,0],[0,1],[0,-1]]
        startColor = image[sr][sc]
        if startColor == newColor:
            return image
        return self.dfs(image,sr,sc,newColor,neighbours,startColor)
    def dfs(self,image,rw,col,newColor,neighbours,startColor):
        image[rw][col] = newColor
        for neighbour in neighbours:
            new_rw = rw + neighbour[0]
            new_col = col + neighbour[1]
            if 0 <= new_rw < len(image) and 0 <= new_col < len(image[0]) and image[new_rw][new_col] == startColor:
                image[new_rw][new_col] = newColor
                self.dfs(image,new_rw,new_col,newColor,neighbours,startColor)
        return image