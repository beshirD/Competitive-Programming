class Solution:
    def numIslands(self, grid):
        numOfIslands = 0
        neighbours = [(-1,0),(1,0),(0,1),(0,-1)]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    self.dfs(grid,row,col,neighbours)
                    numOfIslands += 1
        return numOfIslands
    def dfs(self,grid,i,j,neighbours):
        grid[i][j] = "0"
        for neighbour in neighbours:
            new_row = neighbour[0] + i
            new_col = neighbour[1] + j
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == "1":
                self.dfs(grid,new_row,new_col,neighbours)
                