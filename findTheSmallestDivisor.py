import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start = 1
        end = max(nums)
        while start <= end:
            middle = start + (end - start)//2
            if self.sumDivisions(nums,middle) > threshold:
                start = middle + 1
            else:
                end = middle - 1
        return end + 1
            
    def sumDivisions(self,nums,divisor):
        divisions = []
        for i in nums:
            divisions.append(math.ceil(i/divisor))
        return sum(divisions)
        