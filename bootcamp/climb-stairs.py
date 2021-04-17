class Solution:
    def climbStairs(self, n: int) -> int:
        memory = {}
        def dfs(stair):
            if stair in memory:
                return memory[stair]
            if stair == n - 1:
                return 1
            if stair == n-2:
                return 2
            
            one_step = dfs(stair + 1)
            two_step = dfs(stair + 2)
            memory[stair] = one_step + two_step
            return memory[stair]
        return dfs(0)