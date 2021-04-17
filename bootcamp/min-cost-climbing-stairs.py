from collections import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memory = {}
        def findMin(index):
            if index in memory:
                return memory[index]
            if index == len(cost) - 1 or index == len(cost) - 2:
                return cost[index]
            jump_one = findMin(index + 1)
            jump_two = findMin(index + 2)
            min_cost = min(jump_one,jump_two)
            
            memory[index] = min_cost + cost[index]
            return min_cost + cost[index]
        return min(findMin(0),findMin(1))