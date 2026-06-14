class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]   # ✅ negate for max heap
        heapq.heapify(maxHeap)           # ✅ build the heap

        while len(maxHeap) > 1:
            stone1 = -heapq.heappop(maxHeap)   # ✅ largest (negate back)
            stone2 = -heapq.heappop(maxHeap)   # ✅ second largest

            if stone1 == stone2:               # both destroyed — push nothing
                pass
            else:
                diff = stone1 - stone2         # ✅ stone1 always >= stone2
                heapq.heappush(maxHeap, -diff) # ✅ push back negated

        return -maxHeap[0] if maxHeap else 0