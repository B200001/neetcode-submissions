class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []                                          # ✅ define res

        for i in range(len(points)):
            dist = points[i][0]**2 + points[i][1]**2
            heapq.heappush(minHeap, [dist, points[i][0], points[i][1]])  # ✅ heappush

        while k > 0:
            popped = heapq.heappop(minHeap)               # ✅ () not []
            res.append([popped[1], popped[2]])            # ✅ [1],[2] = x,y not [0](dist)
            k -= 1

        return res