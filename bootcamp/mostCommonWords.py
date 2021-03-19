from collections import List,re,heapq
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        words = re.sub(r'[^\w]', ' ', paragraph).split(" ")
        heap = []
        word_count = {}
        for word in words:
            if word != "":
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        
        for key,value in word_count.items():
            heapq.heappush(heap,(-value,key))
      
        while heap:
            top = heapq.heappop(heap)
           
            if  top[1] not in banned:
                return top[1]
            continue
            
                                                                 