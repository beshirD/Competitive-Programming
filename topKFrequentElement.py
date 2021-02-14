import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap =[]
        result = []
        my_dict = {}
        for itr in nums:
            if itr not in my_dict:
                my_dict[itr] = 1
            else:
                my_dict[itr] += 1
        for key,value in my_dict.items():
            heapq.heappush(heap,(-value,key))
        for i in range(k):
            result.append(heappop(heap)[1])   
        return result