class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memory = {}
        neighbours = [(0,1),(1,0)]
        
        def dfs(rw,col):
            path = 0
            if (rw,col) in memory:
                return memory[(rw,col)]
            
            if rw == m and col == n:
                return 1
            for r , c in neighbours:
                new_r = rw + r
                new_col = col + c
                if 0 < new_r <= m and 0 < new_col <= n:
                    path += dfs(new_r,new_col) 
            memory[(rw,col)] = path
            return path 
        return dfs(1,1)


        