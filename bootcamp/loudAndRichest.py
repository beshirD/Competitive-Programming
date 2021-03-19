from collections import defaultdict,List
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        visited = {}
        answer = [0] * len(quiet)
        for rich in richer:
            graph[rich[1]].append(rich[0]) 
        for person in range(len(quiet)):
            answer[person] = self.dfs(graph,person,quiet,visited)[1]
        print(graph)
        return answer
    def dfs(self,graph,person,quiet,visited):
#         print(person, answer)
#         if not bool(graph[person]):
#             answer[person] = person
#             print(answer)
#         else:
#             for rich in graph[person]:
#                 if quiet[person] > quiet[rich]:
#                     answer[person] = rich
#                 self.dfs(graph,rich,quiet,answer)
        
        if not bool(graph[person]):
            return (quiet[person],person)
        ans = (quiet[person],person)
        for rich in graph[person]:
            if rich not in visited:
                val = self.dfs(graph,rich,quiet,visited)
                if val[0] < ans[0]:
                    ans = val
                visited[rich] = val
                    
            else:
                if visited[rich][0] < ans[0]:
                    ans = visited[rich]
                    
        return ans
         

            