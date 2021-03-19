from collections import deque , List
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        visited = set()
        queue = deque()
        size = len(seats)
        neighbours = [-1,1]
        max_dist = 0
        for i in range(len(seats)):
            if seats[i] == 1 :
                visited.add(i)
                queue.append((i,0))
        while queue:
            seat , dist = queue.popleft()
            for neighbour in neighbours:
                new_seat = seat + neighbour
                if 0 <= new_seat < size and new_seat not in visited:
                    visited.add(new_seat)
                    queue.append((new_seat,dist + 1))
            max_dist = max(max_dist, dist)
        return max_dist
       