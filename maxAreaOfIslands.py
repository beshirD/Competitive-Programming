class Solution:
    def maxAreaOfIsland(self, grid):
        neighbours = [(-1,0),(1,0),(0,1),(0,-1)]
        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    count = [0]
                    self.dfs(grid,row,col,count,neighbours)
                    maxArea = max(maxArea,count[0])
        return maxArea
    def dfs(self,grid,row,col,count,neighbours):
        count[0] += 1
        grid[row][col] = 0
        for neighbour in neighbours:
            new_row = neighbour[0] + row
            new_col = neighbour[1] + col
            if  0 <= new_row < len(grid) and \
                0 <= new_col < len(grid[0]) \
                and grid[new_row][new_col] == 1:
                    self.dfs(grid,new_row,new_col,count,neighbours)
                    
                    
            
            