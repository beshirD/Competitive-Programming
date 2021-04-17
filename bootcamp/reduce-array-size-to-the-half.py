from collections import Counter , List ,heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count_dict = Counter(arr) # O(n)
        min_size = 1
        heap = []
        total = 0
        max_count = max(count_dict.values())
        for key,value in count_dict.items(): # O(n)
            heapq.heappush(heap,(-value,key))
        
        total = (-1 * heap[0][0]) 
        while total < len(arr)//2: # O(n/2)
            
            min_size += 1
            heapq.heappop(heap)
            total += (-1 * heap[0][0]) 
        
        return min_size
                