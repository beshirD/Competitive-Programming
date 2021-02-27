from collections import deque,defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        result = []
        countArray = [0] * numCourses 
        queue = deque()
        for edges in prerequisites:
            countArray[edges[0]] += 1   
            graph[edges[1]].append(edges[0])
        change = None
        for i in countArray:
            if i == 0:
                idx = countArray.index(i)
                queue.append(idx)
                countArray[idx] = change
        while queue:
            node = queue.popleft()
            result.append(node)
            for child in graph[node]:        
                countArray[child] -= 1
                if countArray[child] == 0:
                    queue.append(child)
                    countArray[child] = change
        if len(result) == numCourses:
            return True
        else:
            return False
                  
        