class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heaps = []
        for x,y in points:
            dist = x**2 + y**2
            heapq.heappush(heaps,(-dist,(x,y)))
            if len(heaps)>k:
                heapq.heappop(heaps)
            
        return [points for dist ,points in heaps]
        