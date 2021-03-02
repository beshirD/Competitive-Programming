
from collections import deque
class Solution:
    def maxDistance(self, grid):
        neighbours = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque()
        distance = -1
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] == 1:
                    queue.append((row,col,0))
     
        while queue:
            rw ,col,distance = queue.popleft()
            for neighbour in neighbours:
                new_row = rw + neighbour[0]
                new_col = col + neighbour[1]
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid) and grid[new_row][new_col] == 0:
                    grid[new_row][new_col] = 1
                    queue.append((new_row,new_col,distance + 1))
        if distance == 0:
            return -1
        return distance 
            