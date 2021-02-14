import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        heapq.heapify(nums)
        for i in range(len(nums)):
            heap.append(heapq.heappop(nums))
        return heap