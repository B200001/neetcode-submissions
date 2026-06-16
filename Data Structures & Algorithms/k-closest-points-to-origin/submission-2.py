class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean = lambda x,y : x*x + y*y
        minHeap = []

        for l, r in points:
            dis = euclidean(l, r)
            heapq.heappush(minHeap, [dis, l, r])
        res = []

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        
        return res