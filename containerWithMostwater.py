class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] <= height[j]:   
                maxArea = max(maxArea, height[i] * (j - i))
                i += 1
            elif height[i] >= height[j]:
                maxArea = max(maxArea, height[j] * (j - i))
                j -= 1
        return maxArea