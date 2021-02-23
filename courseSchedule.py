from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        my_dict = {}
        result = []
        countArray = [0] * numCourses 
        queue = deque()
        for edges in prerequisites:
            countArray[edges[0]] += 1
            if edges[1] in my_dict:
                my_dict[edges[1]].append(edges[0])
            else:
                my_dict[edges[1]] = [edges[0]] 
        change = None
        for i in countArray:
            if i == 0:
                idx = countArray.index(i)
                queue.append(idx)
                countArray[idx] = change
        while queue:
            node = queue.popleft()
            result.append(node)
            for parent,child in my_dict.items():
                if parent == node:
                    for i in child:
                        countArray[i] -= 1
                        if countArray[i] == 0:
                            queue.append(i)
                            countArray[i] = change
        if len(result) == numCourses:
            return True
        else:
            return False
                  
        