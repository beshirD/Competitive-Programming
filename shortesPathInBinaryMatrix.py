from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        queue = deque()
        neighbours = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        if grid[0][0] == 0 and grid[len(grid) -1][len(grid) -1] == 0:
            grid[0][0] = 1
            queue.append((0,0,1))
        else:
            return -1
        while queue:
            row , col , lenOfPath = queue.popleft()
            for neighbour in neighbours:
                new_row = row + neighbour[0]
                new_col = col + neighbour[1]
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid) and grid[new_row][new_col] == 0:
                    grid[new_row][new_col] = 1
                    queue.append((new_row,new_col,lenOfPath + 1))
            if (row,col) == (len(grid)- 1 , len(grid) - 1):
                return lenOfPath
        return -1