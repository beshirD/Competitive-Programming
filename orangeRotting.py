from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minMinute = 0
        neighbours = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        for rw in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[rw][col] == 2:
                    queue.append((rw,col,0))
        while queue:
            row, col , minMinute = queue.popleft()
            for neighbour in neighbours:
                new_row = row + neighbour[0]
                new_col = col + neighbour[1]
                if 0 <= new_row < len(grid) \
                    and 0 <= new_col < len(grid[0]) \
                    and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    queue.append((new_row,new_col,minMinute + 1))
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return minMinute
                    
            
            