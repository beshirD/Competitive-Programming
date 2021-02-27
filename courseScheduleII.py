from collections import deque,defaultdict
class Solution:
    def findOrder(self, numCourses, prerequisites):
#         visited = [False] * numCourses
#         stack = []
#         graph = {}
#         for edges in prerequisites:
#             if edges[1] in graph:
#                 graph[edges[1]].append(edges[0])
#             else:
#                 graph[edges[1]] = [edges[0]] 
#         for node in range(numCourses):
#             if visited[node] == False:
#                 self.dfs(node,visited,stack,graph)
#         return stack[::-1]
#     def dfs(self,node,visited,stack,graph):
#         visited[node] = True
#         if node in graph:
#             for child in graph[node]:
#                 if visited[child] == False:
#                     self.dfs(child,visited,stack,graph)
#         stack.append(node)
        
        
        
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
        if len(result) != numCourses:
            return []
        return result                 