from collections import List , heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count = {}
        heap = []
        result = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if i in count:
                        count[i] += 1
                    else:
                        count[i] = 1
                else:
                    if i not in count:
                        count[i] = 0
        
        for key ,value in count.items():
            heapq.heappush(heap,(value,key))
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
            