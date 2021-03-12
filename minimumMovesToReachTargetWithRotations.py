from collections import deque , List
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        visited = set()
        neighbours = [
            [(1,0),(1,0)],
            [(0,1),(0,1)],
            [(1,-1),(0,0)],
            [(-1,1),(0,0)]]
        queue = deque([((0,0),(0,1),0)])
        visited.add(((0,0),(0,1)))
    
        while queue:
            tail , head , min_dis = queue.popleft()
            
            if tail == ((len(grid)-1),(len(grid)-2)) and head == ((len(grid)-1),(len(grid)-1)):
                return min_dis
            
            for neigh in neighbours:
                new_head = (head[0] + neigh[0][0] , head[1] + neigh[0][1])    
                new_tail = (tail[0] + neigh[1][0] , tail[1] + neigh[1][1])
               
                if neigh == neighbours[2]:
                   
                    if self.validate(visited,neighbours,new_tail,new_head,grid) and self.validateCW(grid,tail,head):
                        visited.add(((new_tail),(new_head)))
                        queue.append(((new_tail),(new_head),min_dis + 1))
                elif neigh == neighbours[3]:
                    
                    if self.validate(visited,neighbours,new_tail,new_head,grid) and self.validateCounterCW(grid,tail,head):
                        
                        visited.add(((new_tail),(new_head)))
                        queue.append(((new_tail),(new_head),min_dis + 1))
                        
                else:
                   
                   
                    if self.validate(visited,neighbours,new_tail,new_head,grid):
                        
                        visited.add(((new_tail),(new_head)))
                        queue.append(((new_tail),(new_head),min_dis + 1))
            
                    
        return -1  
    def validate(self,visited,neighbours,tail,head,grid):
     
        if  ((tail,head) not in visited and 
            0 <= tail[0] < len(grid) and 
            0 <= tail[1] < len(grid) and 
            0 <= head[0] < len(grid) and 
            0 <= head[1] < len(grid) and 
            grid[tail[0]][tail[1]] != 1 and 
            grid[head[0]][head[1]] != 1):
        
                return True
        
        return False
        
    def validateCW(self,grid,tail,head):
       
        if grid[tail[0] + 1][tail[1]] == 0 and grid[head[0] + 1][head[1]] == 0 and tail[0] == head[0]:
            return True
        else:
            return False
    def validateCounterCW(self,grid,tail,head):
        if grid[tail[0]][tail[1] + 1] == 0 and grid[head[0]][head[1] + 1 ] == 0 and tail[1] == head[1]:
            return True
        else:
            return False
            
        
        