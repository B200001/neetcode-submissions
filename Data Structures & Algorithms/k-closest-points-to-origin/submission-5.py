import heapq
class Solution:
    def ed(self, x1, y1):
        return x1 ** 2 + y1 ** 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        one = []
        heapq.heapify(one)

        for i in range(len(points)):
            dist = self.ed(points[i][0], points[i][1])
            heapq.heappush(one, [dist, points[i][0], points[i][1]])

        
        result = heapq.nsmallest(k, one)
        return [[point[1], point[2]] for point in result] 
        
        
        
        