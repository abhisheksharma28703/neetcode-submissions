import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        ans = []
        heapq.heapify(h)
        for i in range(len(points)):
            dist = math.sqrt(points[i][0]*points[i][0] + points[i][1]*points[i][1])
            heapq.heappush(h,(dist,(points[i][0],points[i][1])))

        while k>0:
            temp = heapq.heappop(h)[1]
            ans.append(temp)
            k -= 1
        return ans
 