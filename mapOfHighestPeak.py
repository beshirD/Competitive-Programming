from collections import deque
class Solution:
    def highestPeak(self, isWater):
        queue = deque()
        neighbours = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        for rw in range(len(isWater)):
            for col in range(len(isWater[0])):
                if isWater[rw][col] == 1 and (rw,col) not in visited:
                    isWater[rw][col] = 0
                    visited.add((rw,col))
                    queue.append((rw,col,0))
        while queue:
            row , col , height = queue.popleft()
            for neighbour in neighbours:
                new_row = row + neighbour[0]
                new_col = col + neighbour[1]
                if 0 <= new_row < len(isWater) and 0 <= new_col < len(isWater[0]) and (new_row,new_col) not in visited:
                    visited.add((new_row,new_col))
                    isWater[new_row][new_col] = height + 1
                    queue.append((new_row,new_col,height + 1))
        return isWater