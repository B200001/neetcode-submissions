class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        maxheap = []
        # heapq.heapify(maxheap)

        if len(stones) == 1:
            return stones[0]

        for s in stones:
            heapq.heappush(maxheap, -s)
        
        while len(maxheap) > 1:
            
            stone1 = -heapq.heappop(maxheap)
            stone2 = -heapq.heappop(maxheap)
            if stone1 != stone2:
                heapq.heappush(maxheap, -(stone1 - stone2))
            
        
        if len(maxheap) >= 1:
            return -maxheap[0]
        else:
            return 0
        