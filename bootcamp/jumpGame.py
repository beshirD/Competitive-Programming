class Solution:
    def canJump(self, nums) -> bool:
        max_distance = 0
        if nums[0] == 0 and len(nums) > 1:
            return False
     
        for i in range(len(nums)):
            if max_distance >= len(nums) - 1:
                return True
            
            if i > max_distance:
                return False
            
            if max_distance < nums[i] + i:
                max_distance = nums[i] + i  
                
        return False