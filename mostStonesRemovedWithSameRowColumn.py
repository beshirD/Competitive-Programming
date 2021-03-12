
from collections import defaultdict,List
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        count = [0]
        stone_dict = defaultdict(list)
        visited = set()
        for i in range(len(stones)):
            for j in range(len(stones)):
                if i != j:
                    if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                        stone_dict[tuple(stones[i])].append(tuple(stones[j]))
        for stone in stones:
            self.dfs(stone_dict,stone,count,visited)
        return count[0]
    def dfs(self,graph,stone,count,visited):     
        visited.add(tuple(stone))
        for st in graph[tuple(stone)]:
            if st not in visited:
                count[0] += 1
                visited.add((st))
                self.dfs(graph,st,count,visited)
        return count[0]
 
    # def removeStones(self, stones: List[List[int]]) -> int:
    #     count = [0]
    #     stone_dict = defaultdict(list)
    #     visited = set()
        
    #     row = {}  #0: [[0,0]]
    #     col = {}
        
    #     for stone in stones:
    #         r = stone[0]
    #         c = stone[1]
            
    #         if r not in row:
    #             row[r] = [stone]
    #         else:
    #             row[r].append(stone)
            
    #         if c not in col:
    #             col[c] = [stone]
    #         else:
    #             col[c].append(stone)
        
    #     for stone in stones:
    #         state = tuple(stone)
    #         if state not in visited:
    #             visited.add(state)
    #             self.dfs(row,col,stone,count,visited)
        
    #     return count[0]
    
    # def dfs(self,row,col,stone,count,visited):  
    #     state = tuple(stone)
        
    #     for st in row[state[0]]:
    #         stState = tuple(st)
    #         if stState not in visited:
    #             count[0] += 1
    #             visited.add(stState)
    #             self.dfs(row,col,st,count,visited)
        
    #     for st in col[state[1]]:
    #         stState = tuple(st)
    #         if stState not in visited:
    #             count[0] += 1
    #             visited.add(stState)
    #             self.dfs(row,col,st,count,visited)
                
    #     return count[0]