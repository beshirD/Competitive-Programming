"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        for i in range(1,z+1):
            start = 1
            end = z
            while start <= end:
                mid = (start + end)//2
                if customfunction.f(i,mid) == z:
                    result.append([i,mid])
                    break
                elif customfunction.f(i,mid) < z:
                    start = mid + 1
                else:
                    end = mid - 1
        return result