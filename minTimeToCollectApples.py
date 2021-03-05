from collections import deque, Counter , defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])
        visited = set()
    
        return self.dfs(tree,0,visited,hasApple)
        
    def dfs(self,tree,node,visited,hasApple):
        visited.add(node)
        children_cost = 0
        for child in tree[node]:
            if child not in visited:   
                children_cost += self.dfs(tree,child,visited,hasApple)
                
        if children_cost != 0 or hasApple[node]:
            if node != 0:
                return children_cost + 2
            else:
                return children_cost
        return 0
        