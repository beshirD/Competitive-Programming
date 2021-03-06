import heapq
class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        heap = []
        result = []
        if len(nums1) == 0 or len(nums2) == 0 or k == 0:
            return result
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heapq.heappush(heap,(nums1[i] + nums2[j],[nums1[i] ,nums2[j]]))
        for ans in range(k):
            if heap:
                result.append(heapq.heappop(heap)[1])
        return result