from collections import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        memory = {}
        def robHouse(i):
            if i in memory:
                return memory[i]
            if i == len(nums) - 1 or  i == len(nums)-2:
                return nums[i]
            one = robHouse(i + 2)
            two = robHouse(i + 3) if i + 3 < len(nums) else 0
            memory[i] = max(one,two) + nums[i]
            return memory[i]
            
        max_money = 0
        for i in range(len(nums)):
            max_money = max(max_money,robHouse(i))
        return max_money
       