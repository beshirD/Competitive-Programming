import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        heap = []
        resultString = []
        strCount = Counter(S)
        for key,value in strCount.items():
            heapq.heappush(heap,(-value,key))
        heapq.heapify(heap)
        while len(heap) > 1:
            letter1 = heapq.heappop(heap)
            letter2 = heapq.heappop(heap)
            resultString.append(letter1[1])
            resultString.append(letter2[1])
            if letter1[0] < -1:
                heapq.heappush(heap,(letter1[0] + 1, letter1[1]))
            if letter2[0] < -1:
                heapq.heappush(heap,(letter2[0] + 1, letter2[1]))
    
        if heap:
            if heap[0][0] < -1:
                return ""
            resultString.append(heap[0][1])
        return "".join(resultString)
            