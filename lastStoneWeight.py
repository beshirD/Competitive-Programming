import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        while len(stones) > 1:
            twoLargeStones = heapq.nlargest(2,stones)
            x = twoLargeStones[0]
            y = twoLargeStones[1]
            stones.remove(x)
            stones.remove(y)
            if abs(x-y) > 0:
                heapq.heappush(stones,abs(x-y))
        if stones:
            return stones[0]
        return 0
        