import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = []
        heap = []
        my_dict = {}
        for itr in words:
            if itr in my_dict:
                my_dict[itr] += 1
            else:
                my_dict[itr] = 1
        for key,value in my_dict.items():
            heapq.heappush(heap,(-value,key))
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result