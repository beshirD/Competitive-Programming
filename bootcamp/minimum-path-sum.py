from collections import List
class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        neighbours = [(0,1),(1,0)]
        memory = {}
        
            
        def dfs(rw,col):
            if (rw,col) in memory:
                return memory[(rw,col)]
            
            if rw == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[rw][col]
            minimum_sum = float("inf")
            for r,c in neighbours:
                new_rw = r + rw
                new_col = c + col
                if 0 <= new_rw < len(grid) and 0 <= new_col < len(grid[0]):
                    minimum_sum = min(minimum_sum , dfs(new_rw,new_col))
            memory[(rw,col)] = minimum_sum + grid[rw][col]
            return memory[(rw,col)]
        
        
        return dfs(0,0)